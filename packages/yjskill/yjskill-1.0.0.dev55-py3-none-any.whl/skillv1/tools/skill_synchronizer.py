"""
distribute_skill.py
Authors: leibin01(leibin01@baidu.com)
Date: 2024/12/10
"""

import traceback
import json
from enum import Enum
from typing import Optional
from abc import ABCMeta, abstractmethod

import bcelogger
from pydantic import BaseModel
from jobv1.client import job_client
from jobv1.client import job_api_event as event_api
from jobv1.client import job_api_metric as metric_api

from ..client import skill_api_skill as skill_api
from ..client import skill_client


class SyncSkillKind(Enum):
    """
    SyncSkillKind is the kind of the sync skill.
    """

    Edge = "Edge"
    SubCloud = "SubCloud"


class SkillSynchronizerConfig(BaseModel):
    """
    技能同步器配置

    Attributes:
        sync_kind: str, 技能下发类型，Edge:下发到盒子,SubCloud:下发到子平台
        skill_name: str, 技能名称,对应SkillVersionName, e.g. "workspaces/:ws/skills/:localName/versions/:version"
        skill_create_kind: str, 技能创建类型, e.g. "Sync"
        skill_from_kind: str, 技能来源类型, e.g. "Edge"
        vistudio_endpoint: str, 技能服务后端, e.g. "http://ip:port"
        windmill_endpoint: str, windmill服务后端, e.g. "http://ip:port"
        target_names: list[str], 目标设备名称列表,对应DeviceName, e.g. ["workspaces/:ws/devices/:deviceName"]
        org_id: str
        user_id: str
        job_name: str, 技能下发任务名称
        skill_task_name: str, 技能下发子任务名称
        sync_model_succeed_resul: list[str], 模型下发成功结果列表,若模型下发失败则技能下发也失败
    """

    sync_kind: SyncSkillKind

    skill_name: str
    skill_create_kind: str
    skill_from_kind: str
    vistudio_endpoint: str
    windmill_endpoint: str

    target_names: list[str]

    org_id: str
    user_id: str

    job_name: str
    skill_task_name: str
    sync_model_succeed_result: list[str]


class SkillSynchronizer(metaclass=ABCMeta):
    """
    技能同步器
    """

    config: SkillSynchronizerConfig
    skill_version_name: skill_api.SkillVersionName
    skill: skill_api.Skill
    targets: list[dict]  # 下发到的目的地

    skill_cli: skill_client.SkillClient
    job_cli: job_client.JobClient

    __skill_succeed_count = 0
    __skill_failed_count = 0
    __job_succeed_count = 0
    __job_failed_count = 0
    __job_metric_display_name = "技能下发"
    __skill_task_metric_display_name = "技能下发子任务"
    __event_reason_format = "{}（{}）{}"  # 中文名（id）成功/失败原因

    def __init__(self, config: SkillSynchronizerConfig):
        """
        initialize the class.
        """

        self.config = config
        self.skill_version_name = skill_api.new_skill_version_name(
            self.config.skill_name)

        self.__setup()

    def __setup(self):
        """
        设置技能同步器
        """

        self.skill_cli = skill_client.SkillClient(endpoint=self.config.vistudio_endpoint,
                                                  context={"OrgID": self.config.org_id,
                                                           "UserID": self.config.user_id})
        self.job_cli = job_client.JobClient(endpoint=self.config.windmill_endpoint,
                                            context={"OrgID": self.config.org_id,
                                                     "UserID": self.config.user_id})

    def __get_skill(self):
        """
        获取技能信息

        Returns:
            boolean: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        req = skill_api.GetSkillRequest(
            workspaceID=self.skill_version_name.workspace_id,
            localName=self.skill_version_name.local_name,
            version=self.skill_version_name.version)
        try:
            self.skill = self.skill_cli.get_skill(req=req)
            bcelogger.info("GetSkill req=%s, resp=%s", req, self.skill)
            return True, {}
        except Exception as e:
            bcelogger.error("SyncSkillGetSkill %s Failed: %s",
                            self.skill_version_name.local_name,
                            traceback.format_exc())
            return False, {"error": str(e), "reason": "获取技能失败"}

    def __create_metric(self, local_name: metric_api.MetricLocalName,
                        display_name: str,
                        kind: metric_api.MetricKind,
                        data_type: metric_api.DataType,
                        value: list[str],
                        task_name: Optional[str] = None):
        """
        创建metric
        """

        workspace_id = self.skill_version_name.workspace_id
        req = metric_api.CreateMetricRequest(workspace_id=workspace_id,
                                             job_name=self.config.job_name,
                                             display_name=display_name,
                                             local_name=local_name,
                                             kind=kind,
                                             data_type=data_type,
                                             value=value)
        if task_name is not None:
            req.task_name = task_name
        try:
            resp = job_client.create_metric(req)
            bcelogger.debug("CreateMetric req=%s, resp is %s", req, resp)
        except Exception as e:
            bcelogger.error("create_metric create_metric_req= %s, Failed: %s",
                            req.model_dump(by_alias=True),
                            str(e))

    def __create_event(self,
                       kind: event_api.EventKind,
                       reason: str,
                       message: str,
                       task_name: Optional[str] = None):
        """
        创建事件
        """

        workspace_id = self.skill_version_name.workspace_id
        req = event_api.CreateEventRequest(
            workspace_id=workspace_id,
            job_name=self.config.job_name,
            kind=kind,
            reason=reason,
            message=message)
        if task_name is not None:
            req.task_name = task_name
        try:
            resp = job_client.create_event(
                req)
            bcelogger.debug("CreateEvent req=%s, resp=%s", req, resp)
        except Exception as e:
            bcelogger.error("CreateEventFailed req=%s, Failed: %s",
                            req.model_dump(by_alias=True),
                            str(e))

    def __mark_job_failed(self, reason: str, message: str):
        """
        更新job状态为失败
        """

        # job status failed
        self.__create_metric(display_name=self.__job_metric_display_name,
                             local_name=metric_api.MetricLocalName.JobStatus,
                             kind=metric_api.MetricKind.Gauge,
                             data_type=metric_api.DataType.String,
                             value=["Failed"])
        # 失败原因
        self.__create_event(kind=event_api.EventKind.Failed,
                            reason=reason,
                            message=message)

    def __create_skill_failed_metric(self, message: str, reason: str):
        """
        创建技能失败的指标和事件
        """

        self.__create_metric(display_name=self.__skill_metric_display_name,
                             local_name=metric_api.MetricLocalName.Failed,
                             kind=metric_api.MetricKind.Counter,
                             data_type=metric_api.DataType.Int,
                             value=[str(self.__skill_failed_count)])

    def __create_job_failed_metric_event(self, message: str, reason: str):
        """
        创建job失败metric和event
        """

        # job metric
        self.__create_metric(display_name=self.__job_metric_display_name,
                             local_name=metric_api.MetricLocalName.Failed,
                             kind=metric_api.MetricKind.Counter,
                             data_type=metric_api.DataType.Int,
                             value=[str(self.__job_failed_count)])

        # job event
        self.__create_event(kind=event_api.EventKind.Failed,
                            reason=reason,
                            message=message)

    def __sync_skill(self, target: dict):
        """
        下发技能
        1. 对接任务中心

        Args:
            req: SyncSkillRequest, 技能下发请求参数
        Returns:
            bool: 是否下发成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        ok, err, result = self.preprocess_sync_skill(target=target)
        if not ok:
            self.__skill_failed_count += 1
            # skill task metric
            self.__create_metric(task_name=self.config.skill_task_name,
                                 display_name=self.__skill_task_metric_display_name,
                                 local_name=metric_api.MetricLocalName.Failed,
                                 kind=metric_api.MetricKind.Counter,
                                 data_type=metric_api.DataType.Int,
                                 value=[str(self.__skill_failed_count)])
            return False, err

        create_skill_req = result.get("create_skill_request")
        create_skill_extra_data = result.get("extra_data")
        ok, err, skill_resp = self.create_skill(req=create_skill_req,
                                                extra_data=create_skill_extra_data)
        if not ok:
            self.__skill_failed_count += 1
            # skill task metric
            self.__create_metric(display_name=self.__skill_task_metric_display_name,
                                 local_name=metric_api.MetricLocalName.Failed,
                                 kind=metric_api.MetricKind.Counter,
                                 data_type=metric_api.DataType.Int,
                                 value=[str(self.__skill_failed_count)])
            return False, err

        ok, err = self.postprocess_sync_skill(skill=skill_resp, target=target)
        if not ok:
            self.__skill_failed_count += 1
            # skill task metric
            self.__create_metric(task_name=self.config.skill_task_name,
                                 display_name=self.__skill_task_metric_display_name,
                                 local_name=metric_api.MetricLocalName.Failed,
                                 kind=metric_api.MetricKind.Counter,
                                 data_type=metric_api.DataType.Int,
                                 value=[str(self.__skill_failed_count)])
            return False, err

        self.__skill_succeed_count += 1
        # 技能下发成功
        self.__create_metric(task_name=self.config.skill_task_name,
                             local_name=metric_api.MetricLocalName.Success,
                             display_name=self.__skill_task_metric_display_name,
                             kind=metric_api.MetricKind.Counter,
                             data_type=metric_api.DataType.Int,
                             value=[str(self.__skill_succeed_count)])
        return True, {}

    @abstractmethod
    def list_targets(self):
        """
        获取下发目的地列表

        Returns:
            bool: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
            list[dict]: 目标列表
        """

        pass

    @abstractmethod
    def create_skill(self,
                     req: skill_api.CreateSkillRequest,
                     extra_data: dict):
        """
        创建技能

        Args:
            req: skill_api.CreateSkillRequest, 技能创建请求参数
            extra_data: dict,额外参数
        Returns:
            bool: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "创建技能失败"}
            skill: 创建的技能的信息
        """

        pass

    @abstractmethod
    def sync_model(self, target: dict,
                   extra_data: dict):
        """
        下发模型

        Args:
            target: dict, 下发目标
            extra_data: dict, 额外参数
        Returns:
            bool: 是否下发成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        pass

    @abstractmethod
    def preprocess_sync_skill(self, target: dict):
        """
        sync_skill的前处理

        Args:
            target: dict, 下发目标
        Returns:
            bool: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
            dict: {"create_skill_request": skill_api.CreateSkillRequest,
                "extra_data": dict}
        """

        pass

    @abstractmethod
    def postprocess_sync_skill(self, skill: skill_api.Skill, target: dict):
        """
        sync_skill的后处理

        Args:
            skill: skill_api.Skill, 创建后的技能信息
            target: dict, 下发目标
        Returns:
            bool: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        pass

    def run(self):
        """
        执行技能下发逻辑
        """

        bcelogger.info("SyncSkill Start")

        ok, msg = self.__get_skill()
        if not ok:
            self.__mark_job_failed(reason=msg["reason"],
                                   message=msg["error"][:500])
            return

        bcelogger.debug("SyncSkillGetSkill Succeed, skill:%s", self.skill)

        ok, msg, self.targets = self.list_targets()
        if not ok:
            self.__mark_job_failed(reason=msg["reason"],
                                   message=msg["error"][:500])
            return

        bcelogger.debug(
            "SyncSkillListTargets Succeed, targets:%s", self.targets)

        # 要从Artifact的tag取，因为下发是指定了技能的版本
        # skill_tag = []
        # if skill.graph is not None and 'artifact' in skill.graph:
        #     skill_tag = skill.graph['artifact']['tags']
        # bcelogger.debug("SyncSkillSkillTags: %s", skill_tag)

        for target in self.targets:
            bcelogger.info("SyncSkillTargetInfo: %s", target)
            target_displayname = target.get("displayName", "")
            target_id = target.get("localName", None)

            # 下发模型
            sync_model_extra_data = {}
            sync_model_extra_data["model_succeed_result"] = self.config.sync_model_succeed_result
            ok, msg = self.sync_model(
                target=target, extra_data=sync_model_extra_data)
            if not ok:
                self.__skill_failed_count += 1
                self.__job_failed_count += 1

                self.__create_skill_failed_metric(message=msg["error"][:500],
                                                  reason=msg["reason"])
                self.__create_job_failed_metric_event(message=msg["error"][:500],
                                                      reason=msg["reason"])
                continue

            ok, msg = self.__sync_skill(target=target)
            if not ok:
                self.__job_failed_count += 1
                reason = self.__event_reason_format.format(
                    target_displayname, target_id, msg["reason"])
                self.__create_job_failed_metric_event(message=msg["error"][:500],
                                                      reason=reason)
                continue

            # job下发成功
            self.__job_succeed_count += 1
            self.__create_metric(local_name=metric_api.MetricLocalName.Success,
                                 display_name=self.__job_metric_display_name,
                                 kind=metric_api.MetricKind.Counter,
                                 data_type=metric_api.DataType.Int,
                                 value=[str(self.__job_succeed_count)])

            reason = self.__event_reason_format.format(
                target_displayname, target_id, "下发成功")
            self.__create_event(kind=event_api.EventKind.Succeed,
                                reason=reason, message=reason)
            bcelogger.info("SyncSkill End")


def check_accelerators(skill_accelerator: str,
                       target_accelelator: str):
    """
    检查硬件是否匹配

    Args:
        skill_accelerator(str): 技能硬件信息(tag['accelerator'])
        target_accelelator(str): 设备硬件型号
    Returns:
        bool: 是否匹配
        str: 错误信息
    """

    if skill_accelerator == "":
        return True, ""

    if target_accelelator == "":
        return False, "设备硬件不适配"

    # 将技能硬件信息转换为列表
    skill_accelerators = json.loads(skill_accelerator)
    device_accelerators = [target_accelelator]

    for sac in skill_accelerators:
        if sac not in device_accelerators:
            return False, "设备硬件不适配"

    return True, ""


def build_skill_graph(
        origin_graph: dict,
        replace: dict):
    """
    构建graph, 内容替换<old,new>

    Args:
        origin_graph: dict 原始图
        replace: dict 替换关系<old,new>
    Returns:
        dict: 新图
    """

    origin_graph_json = json.dumps(origin_graph)
    for old, new in replace.items():
        origin_graph_json = origin_graph_json.replace(old, new)
    return json.loads(origin_graph_json)
