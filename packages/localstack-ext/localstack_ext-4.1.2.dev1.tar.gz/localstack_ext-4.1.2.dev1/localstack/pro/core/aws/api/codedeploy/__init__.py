from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AdditionalDeploymentStatusInfo = str
AlarmName = str
ApplicationId = str
ApplicationName = str
Arn = str
AutoScalingGroupHook = str
AutoScalingGroupName = str
Boolean = bool
CloudFormationResourceType = str
CommitId = str
DeploymentConfigId = str
DeploymentConfigName = str
DeploymentGroupId = str
DeploymentGroupName = str
DeploymentId = str
Description = str
Duration = int
ECSClusterName = str
ECSServiceName = str
ECSTaskSetIdentifier = str
ECSTaskSetStatus = str
ELBName = str
ETag = str
ErrorMessage = str
ExternalId = str
FilterValue = str
GitHubAccountTokenName = str
IamSessionArn = str
IamUserArn = str
InstanceArn = str
InstanceId = str
InstanceName = str
Key = str
LambdaFunctionAlias = str
LambdaFunctionName = str
LifecycleEventHookExecutionId = str
LifecycleEventName = str
LifecycleMessage = str
ListenerArn = str
LogTail = str
Message = str
MinimumHealthyHostsPerZoneValue = int
MinimumHealthyHostsValue = int
NextToken = str
NullableBoolean = bool
Percentage = int
RawStringContent = str
RawStringSha256 = str
Repository = str
Role = str
S3Bucket = str
S3Key = str
ScriptName = str
TargetArn = str
TargetGroupName = str
TargetId = str
TrafficWeight = float
TriggerName = str
TriggerTargetArn = str
Value = str
Version = str
VersionId = str
WaitTimeInMins = int


class ApplicationRevisionSortBy(StrEnum):
    registerTime = "registerTime"
    firstUsedTime = "firstUsedTime"
    lastUsedTime = "lastUsedTime"


class AutoRollbackEvent(StrEnum):
    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    DEPLOYMENT_STOP_ON_ALARM = "DEPLOYMENT_STOP_ON_ALARM"
    DEPLOYMENT_STOP_ON_REQUEST = "DEPLOYMENT_STOP_ON_REQUEST"


class BundleType(StrEnum):
    tar = "tar"
    tgz = "tgz"
    zip = "zip"
    YAML = "YAML"
    JSON = "JSON"


class ComputePlatform(StrEnum):
    Server = "Server"
    Lambda = "Lambda"
    ECS = "ECS"


class DeploymentCreator(StrEnum):
    user = "user"
    autoscaling = "autoscaling"
    codeDeployRollback = "codeDeployRollback"
    CodeDeploy = "CodeDeploy"
    CodeDeployAutoUpdate = "CodeDeployAutoUpdate"
    CloudFormation = "CloudFormation"
    CloudFormationRollback = "CloudFormationRollback"
    autoscalingTermination = "autoscalingTermination"


class DeploymentOption(StrEnum):
    WITH_TRAFFIC_CONTROL = "WITH_TRAFFIC_CONTROL"
    WITHOUT_TRAFFIC_CONTROL = "WITHOUT_TRAFFIC_CONTROL"


class DeploymentReadyAction(StrEnum):
    CONTINUE_DEPLOYMENT = "CONTINUE_DEPLOYMENT"
    STOP_DEPLOYMENT = "STOP_DEPLOYMENT"


class DeploymentStatus(StrEnum):
    Created = "Created"
    Queued = "Queued"
    InProgress = "InProgress"
    Baking = "Baking"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Stopped = "Stopped"
    Ready = "Ready"


class DeploymentTargetType(StrEnum):
    InstanceTarget = "InstanceTarget"
    LambdaTarget = "LambdaTarget"
    ECSTarget = "ECSTarget"
    CloudFormationTarget = "CloudFormationTarget"


class DeploymentType(StrEnum):
    IN_PLACE = "IN_PLACE"
    BLUE_GREEN = "BLUE_GREEN"


class DeploymentWaitType(StrEnum):
    READY_WAIT = "READY_WAIT"
    TERMINATION_WAIT = "TERMINATION_WAIT"


class EC2TagFilterType(StrEnum):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class ErrorCode(StrEnum):
    AGENT_ISSUE = "AGENT_ISSUE"
    ALARM_ACTIVE = "ALARM_ACTIVE"
    APPLICATION_MISSING = "APPLICATION_MISSING"
    AUTOSCALING_VALIDATION_ERROR = "AUTOSCALING_VALIDATION_ERROR"
    AUTO_SCALING_CONFIGURATION = "AUTO_SCALING_CONFIGURATION"
    AUTO_SCALING_IAM_ROLE_PERMISSIONS = "AUTO_SCALING_IAM_ROLE_PERMISSIONS"
    CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND = "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND"
    CUSTOMER_APPLICATION_UNHEALTHY = "CUSTOMER_APPLICATION_UNHEALTHY"
    DEPLOYMENT_GROUP_MISSING = "DEPLOYMENT_GROUP_MISSING"
    ECS_UPDATE_ERROR = "ECS_UPDATE_ERROR"
    ELASTIC_LOAD_BALANCING_INVALID = "ELASTIC_LOAD_BALANCING_INVALID"
    ELB_INVALID_INSTANCE = "ELB_INVALID_INSTANCE"
    HEALTH_CONSTRAINTS = "HEALTH_CONSTRAINTS"
    HEALTH_CONSTRAINTS_INVALID = "HEALTH_CONSTRAINTS_INVALID"
    HOOK_EXECUTION_FAILURE = "HOOK_EXECUTION_FAILURE"
    IAM_ROLE_MISSING = "IAM_ROLE_MISSING"
    IAM_ROLE_PERMISSIONS = "IAM_ROLE_PERMISSIONS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_ECS_SERVICE = "INVALID_ECS_SERVICE"
    INVALID_LAMBDA_CONFIGURATION = "INVALID_LAMBDA_CONFIGURATION"
    INVALID_LAMBDA_FUNCTION = "INVALID_LAMBDA_FUNCTION"
    INVALID_REVISION = "INVALID_REVISION"
    MANUAL_STOP = "MANUAL_STOP"
    MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION = "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION"
    MISSING_ELB_INFORMATION = "MISSING_ELB_INFORMATION"
    MISSING_GITHUB_TOKEN = "MISSING_GITHUB_TOKEN"
    NO_EC2_SUBSCRIPTION = "NO_EC2_SUBSCRIPTION"
    NO_INSTANCES = "NO_INSTANCES"
    OVER_MAX_INSTANCES = "OVER_MAX_INSTANCES"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    REVISION_MISSING = "REVISION_MISSING"
    THROTTLED = "THROTTLED"
    TIMEOUT = "TIMEOUT"
    CLOUDFORMATION_STACK_FAILURE = "CLOUDFORMATION_STACK_FAILURE"


class FileExistsBehavior(StrEnum):
    DISALLOW = "DISALLOW"
    OVERWRITE = "OVERWRITE"
    RETAIN = "RETAIN"


class GreenFleetProvisioningAction(StrEnum):
    DISCOVER_EXISTING = "DISCOVER_EXISTING"
    COPY_AUTO_SCALING_GROUP = "COPY_AUTO_SCALING_GROUP"


class InstanceAction(StrEnum):
    TERMINATE = "TERMINATE"
    KEEP_ALIVE = "KEEP_ALIVE"


class InstanceStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"
    Ready = "Ready"


class InstanceType(StrEnum):
    Blue = "Blue"
    Green = "Green"


class LifecycleErrorCode(StrEnum):
    Success = "Success"
    ScriptMissing = "ScriptMissing"
    ScriptNotExecutable = "ScriptNotExecutable"
    ScriptTimedOut = "ScriptTimedOut"
    ScriptFailed = "ScriptFailed"
    UnknownError = "UnknownError"


class LifecycleEventStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"


class ListStateFilterAction(StrEnum):
    include = "include"
    exclude = "exclude"
    ignore = "ignore"


class MinimumHealthyHostsPerZoneType(StrEnum):
    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class MinimumHealthyHostsType(StrEnum):
    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class OutdatedInstancesStrategy(StrEnum):
    UPDATE = "UPDATE"
    IGNORE = "IGNORE"


class RegistrationStatus(StrEnum):
    Registered = "Registered"
    Deregistered = "Deregistered"


class RevisionLocationType(StrEnum):
    S3 = "S3"
    GitHub = "GitHub"
    String = "String"
    AppSpecContent = "AppSpecContent"


class SortOrder(StrEnum):
    ascending = "ascending"
    descending = "descending"


class StopStatus(StrEnum):
    Pending = "Pending"
    Succeeded = "Succeeded"


class TagFilterType(StrEnum):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class TargetFilterName(StrEnum):
    TargetStatus = "TargetStatus"
    ServerInstanceLabel = "ServerInstanceLabel"


class TargetLabel(StrEnum):
    Blue = "Blue"
    Green = "Green"


class TargetStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"
    Ready = "Ready"


class TrafficRoutingType(StrEnum):
    TimeBasedCanary = "TimeBasedCanary"
    TimeBasedLinear = "TimeBasedLinear"
    AllAtOnce = "AllAtOnce"


class TriggerEventType(StrEnum):
    DeploymentStart = "DeploymentStart"
    DeploymentSuccess = "DeploymentSuccess"
    DeploymentFailure = "DeploymentFailure"
    DeploymentStop = "DeploymentStop"
    DeploymentRollback = "DeploymentRollback"
    DeploymentReady = "DeploymentReady"
    InstanceStart = "InstanceStart"
    InstanceSuccess = "InstanceSuccess"
    InstanceFailure = "InstanceFailure"
    InstanceReady = "InstanceReady"


class AlarmsLimitExceededException(ServiceException):
    code: str = "AlarmsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationAlreadyExistsException(ServiceException):
    code: str = "ApplicationAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationDoesNotExistException(ServiceException):
    code: str = "ApplicationDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationLimitExceededException(ServiceException):
    code: str = "ApplicationLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationNameRequiredException(ServiceException):
    code: str = "ApplicationNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class ArnNotSupportedException(ServiceException):
    code: str = "ArnNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class BatchLimitExceededException(ServiceException):
    code: str = "BatchLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class BucketNameFilterRequiredException(ServiceException):
    code: str = "BucketNameFilterRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentAlreadyCompletedException(ServiceException):
    code: str = "DeploymentAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentAlreadyStartedException(ServiceException):
    code: str = "DeploymentAlreadyStartedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigAlreadyExistsException(ServiceException):
    code: str = "DeploymentConfigAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigDoesNotExistException(ServiceException):
    code: str = "DeploymentConfigDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigInUseException(ServiceException):
    code: str = "DeploymentConfigInUseException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigLimitExceededException(ServiceException):
    code: str = "DeploymentConfigLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigNameRequiredException(ServiceException):
    code: str = "DeploymentConfigNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentDoesNotExistException(ServiceException):
    code: str = "DeploymentDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupAlreadyExistsException(ServiceException):
    code: str = "DeploymentGroupAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupDoesNotExistException(ServiceException):
    code: str = "DeploymentGroupDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupLimitExceededException(ServiceException):
    code: str = "DeploymentGroupLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupNameRequiredException(ServiceException):
    code: str = "DeploymentGroupNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentIdRequiredException(ServiceException):
    code: str = "DeploymentIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentIsNotInReadyStateException(ServiceException):
    code: str = "DeploymentIsNotInReadyStateException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentLimitExceededException(ServiceException):
    code: str = "DeploymentLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentNotStartedException(ServiceException):
    code: str = "DeploymentNotStartedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetDoesNotExistException(ServiceException):
    code: str = "DeploymentTargetDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetIdRequiredException(ServiceException):
    code: str = "DeploymentTargetIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetListSizeExceededException(ServiceException):
    code: str = "DeploymentTargetListSizeExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DescriptionTooLongException(ServiceException):
    code: str = "DescriptionTooLongException"
    sender_fault: bool = False
    status_code: int = 400


class ECSServiceMappingLimitExceededException(ServiceException):
    code: str = "ECSServiceMappingLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class GitHubAccountTokenDoesNotExistException(ServiceException):
    code: str = "GitHubAccountTokenDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class GitHubAccountTokenNameRequiredException(ServiceException):
    code: str = "GitHubAccountTokenNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class IamArnRequiredException(ServiceException):
    code: str = "IamArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class IamSessionArnAlreadyRegisteredException(ServiceException):
    code: str = "IamSessionArnAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class IamUserArnAlreadyRegisteredException(ServiceException):
    code: str = "IamUserArnAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class IamUserArnRequiredException(ServiceException):
    code: str = "IamUserArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceDoesNotExistException(ServiceException):
    code: str = "InstanceDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceIdRequiredException(ServiceException):
    code: str = "InstanceIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceLimitExceededException(ServiceException):
    code: str = "InstanceLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNameAlreadyRegisteredException(ServiceException):
    code: str = "InstanceNameAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNameRequiredException(ServiceException):
    code: str = "InstanceNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNotRegisteredException(ServiceException):
    code: str = "InstanceNotRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAlarmConfigException(ServiceException):
    code: str = "InvalidAlarmConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidApplicationNameException(ServiceException):
    code: str = "InvalidApplicationNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidArnException(ServiceException):
    code: str = "InvalidArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAutoRollbackConfigException(ServiceException):
    code: str = "InvalidAutoRollbackConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAutoScalingGroupException(ServiceException):
    code: str = "InvalidAutoScalingGroupException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBlueGreenDeploymentConfigurationException(ServiceException):
    code: str = "InvalidBlueGreenDeploymentConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBucketNameFilterException(ServiceException):
    code: str = "InvalidBucketNameFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidComputePlatformException(ServiceException):
    code: str = "InvalidComputePlatformException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeployedStateFilterException(ServiceException):
    code: str = "InvalidDeployedStateFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentConfigNameException(ServiceException):
    code: str = "InvalidDeploymentConfigNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentGroupNameException(ServiceException):
    code: str = "InvalidDeploymentGroupNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentIdException(ServiceException):
    code: str = "InvalidDeploymentIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentInstanceTypeException(ServiceException):
    code: str = "InvalidDeploymentInstanceTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentStatusException(ServiceException):
    code: str = "InvalidDeploymentStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentStyleException(ServiceException):
    code: str = "InvalidDeploymentStyleException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentTargetIdException(ServiceException):
    code: str = "InvalidDeploymentTargetIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentWaitTypeException(ServiceException):
    code: str = "InvalidDeploymentWaitTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEC2TagCombinationException(ServiceException):
    code: str = "InvalidEC2TagCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEC2TagException(ServiceException):
    code: str = "InvalidEC2TagException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidECSServiceException(ServiceException):
    code: str = "InvalidECSServiceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidExternalIdException(ServiceException):
    code: str = "InvalidExternalIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidFileExistsBehaviorException(ServiceException):
    code: str = "InvalidFileExistsBehaviorException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidGitHubAccountTokenException(ServiceException):
    code: str = "InvalidGitHubAccountTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidGitHubAccountTokenNameException(ServiceException):
    code: str = "InvalidGitHubAccountTokenNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIamSessionArnException(ServiceException):
    code: str = "InvalidIamSessionArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIamUserArnException(ServiceException):
    code: str = "InvalidIamUserArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIgnoreApplicationStopFailuresValueException(ServiceException):
    code: str = "InvalidIgnoreApplicationStopFailuresValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceIdException(ServiceException):
    code: str = "InvalidInstanceIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceNameException(ServiceException):
    code: str = "InvalidInstanceNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceStatusException(ServiceException):
    code: str = "InvalidInstanceStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceTypeException(ServiceException):
    code: str = "InvalidInstanceTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidKeyPrefixFilterException(ServiceException):
    code: str = "InvalidKeyPrefixFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLifecycleEventHookExecutionIdException(ServiceException):
    code: str = "InvalidLifecycleEventHookExecutionIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLifecycleEventHookExecutionStatusException(ServiceException):
    code: str = "InvalidLifecycleEventHookExecutionStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLoadBalancerInfoException(ServiceException):
    code: str = "InvalidLoadBalancerInfoException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidMinimumHealthyHostValueException(ServiceException):
    code: str = "InvalidMinimumHealthyHostValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOnPremisesTagCombinationException(ServiceException):
    code: str = "InvalidOnPremisesTagCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOperationException(ServiceException):
    code: str = "InvalidOperationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRegistrationStatusException(ServiceException):
    code: str = "InvalidRegistrationStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRevisionException(ServiceException):
    code: str = "InvalidRevisionException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRoleException(ServiceException):
    code: str = "InvalidRoleException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSortByException(ServiceException):
    code: str = "InvalidSortByException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSortOrderException(ServiceException):
    code: str = "InvalidSortOrderException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagException(ServiceException):
    code: str = "InvalidTagException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagFilterException(ServiceException):
    code: str = "InvalidTagFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagsToAddException(ServiceException):
    code: str = "InvalidTagsToAddException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetException(ServiceException):
    code: str = "InvalidTargetException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetFilterNameException(ServiceException):
    code: str = "InvalidTargetFilterNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetGroupPairException(ServiceException):
    code: str = "InvalidTargetGroupPairException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetInstancesException(ServiceException):
    code: str = "InvalidTargetInstancesException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTimeRangeException(ServiceException):
    code: str = "InvalidTimeRangeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTrafficRoutingConfigurationException(ServiceException):
    code: str = "InvalidTrafficRoutingConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTriggerConfigException(ServiceException):
    code: str = "InvalidTriggerConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidUpdateOutdatedInstancesOnlyValueException(ServiceException):
    code: str = "InvalidUpdateOutdatedInstancesOnlyValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidZonalDeploymentConfigurationException(ServiceException):
    code: str = "InvalidZonalDeploymentConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class LifecycleEventAlreadyCompletedException(ServiceException):
    code: str = "LifecycleEventAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class LifecycleHookLimitExceededException(ServiceException):
    code: str = "LifecycleHookLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class MultipleIamArnsProvidedException(ServiceException):
    code: str = "MultipleIamArnsProvidedException"
    sender_fault: bool = False
    status_code: int = 400


class OperationNotSupportedException(ServiceException):
    code: str = "OperationNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceArnRequiredException(ServiceException):
    code: str = "ResourceArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceValidationException(ServiceException):
    code: str = "ResourceValidationException"
    sender_fault: bool = False
    status_code: int = 400


class RevisionDoesNotExistException(ServiceException):
    code: str = "RevisionDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class RevisionRequiredException(ServiceException):
    code: str = "RevisionRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class RoleRequiredException(ServiceException):
    code: str = "RoleRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class TagLimitExceededException(ServiceException):
    code: str = "TagLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class TagRequiredException(ServiceException):
    code: str = "TagRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class TagSetListLimitExceededException(ServiceException):
    code: str = "TagSetListLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class TriggerTargetsLimitExceededException(ServiceException):
    code: str = "TriggerTargetsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedActionForDeploymentTypeException(ServiceException):
    code: str = "UnsupportedActionForDeploymentTypeException"
    sender_fault: bool = False
    status_code: int = 400


InstanceNameList = List[InstanceName]


class Tag(TypedDict, total=False):
    Key: Optional[Key]
    Value: Optional[Value]


TagList = List[Tag]


class AddTagsToOnPremisesInstancesInput(ServiceRequest):
    tags: TagList
    instanceNames: InstanceNameList


class Alarm(TypedDict, total=False):
    name: Optional[AlarmName]


AlarmList = List[Alarm]


class AlarmConfiguration(TypedDict, total=False):
    enabled: Optional[Boolean]
    ignorePollAlarmFailure: Optional[Boolean]
    alarms: Optional[AlarmList]


class AppSpecContent(TypedDict, total=False):
    content: Optional[RawStringContent]
    sha256: Optional[RawStringSha256]


Timestamp = datetime


class ApplicationInfo(TypedDict, total=False):
    applicationId: Optional[ApplicationId]
    applicationName: Optional[ApplicationName]
    createTime: Optional[Timestamp]
    linkedToGitHub: Optional[Boolean]
    gitHubAccountName: Optional[GitHubAccountTokenName]
    computePlatform: Optional[ComputePlatform]


ApplicationsInfoList = List[ApplicationInfo]
ApplicationsList = List[ApplicationName]
AutoRollbackEventsList = List[AutoRollbackEvent]


class AutoRollbackConfiguration(TypedDict, total=False):
    enabled: Optional[Boolean]
    events: Optional[AutoRollbackEventsList]


class AutoScalingGroup(TypedDict, total=False):
    name: Optional[AutoScalingGroupName]
    hook: Optional[AutoScalingGroupHook]
    terminationHook: Optional[AutoScalingGroupHook]


AutoScalingGroupList = List[AutoScalingGroup]
AutoScalingGroupNameList = List[AutoScalingGroupName]


class RawString(TypedDict, total=False):
    content: Optional[RawStringContent]
    sha256: Optional[RawStringSha256]


class GitHubLocation(TypedDict, total=False):
    repository: Optional[Repository]
    commitId: Optional[CommitId]


class S3Location(TypedDict, total=False):
    bucket: Optional[S3Bucket]
    key: Optional[S3Key]
    bundleType: Optional[BundleType]
    version: Optional[VersionId]
    eTag: Optional[ETag]


class RevisionLocation(TypedDict, total=False):
    revisionType: Optional[RevisionLocationType]
    s3Location: Optional[S3Location]
    gitHubLocation: Optional[GitHubLocation]
    string: Optional[RawString]
    appSpecContent: Optional[AppSpecContent]


RevisionLocationList = List[RevisionLocation]


class BatchGetApplicationRevisionsInput(ServiceRequest):
    applicationName: ApplicationName
    revisions: RevisionLocationList


DeploymentGroupsList = List[DeploymentGroupName]


class GenericRevisionInfo(TypedDict, total=False):
    description: Optional[Description]
    deploymentGroups: Optional[DeploymentGroupsList]
    firstUsedTime: Optional[Timestamp]
    lastUsedTime: Optional[Timestamp]
    registerTime: Optional[Timestamp]


class RevisionInfo(TypedDict, total=False):
    revisionLocation: Optional[RevisionLocation]
    genericRevisionInfo: Optional[GenericRevisionInfo]


RevisionInfoList = List[RevisionInfo]


class BatchGetApplicationRevisionsOutput(TypedDict, total=False):
    applicationName: Optional[ApplicationName]
    errorMessage: Optional[ErrorMessage]
    revisions: Optional[RevisionInfoList]


class BatchGetApplicationsInput(ServiceRequest):
    applicationNames: ApplicationsList


class BatchGetApplicationsOutput(TypedDict, total=False):
    applicationsInfo: Optional[ApplicationsInfoList]


class BatchGetDeploymentGroupsInput(ServiceRequest):
    applicationName: ApplicationName
    deploymentGroupNames: DeploymentGroupsList


class ECSService(TypedDict, total=False):
    serviceName: Optional[ECSServiceName]
    clusterName: Optional[ECSClusterName]


ECSServiceList = List[ECSService]


class TagFilter(TypedDict, total=False):
    Key: Optional[Key]
    Value: Optional[Value]
    Type: Optional[TagFilterType]


TagFilterList = List[TagFilter]
OnPremisesTagSetList = List[TagFilterList]


class OnPremisesTagSet(TypedDict, total=False):
    onPremisesTagSetList: Optional[OnPremisesTagSetList]


class EC2TagFilter(TypedDict, total=False):
    Key: Optional[Key]
    Value: Optional[Value]
    Type: Optional[EC2TagFilterType]


EC2TagFilterList = List[EC2TagFilter]
EC2TagSetList = List[EC2TagFilterList]


class EC2TagSet(TypedDict, total=False):
    ec2TagSetList: Optional[EC2TagSetList]


class LastDeploymentInfo(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    status: Optional[DeploymentStatus]
    endTime: Optional[Timestamp]
    createTime: Optional[Timestamp]


ListenerArnList = List[ListenerArn]


class TrafficRoute(TypedDict, total=False):
    listenerArns: Optional[ListenerArnList]


class TargetGroupInfo(TypedDict, total=False):
    name: Optional[TargetGroupName]


TargetGroupInfoList = List[TargetGroupInfo]


class TargetGroupPairInfo(TypedDict, total=False):
    targetGroups: Optional[TargetGroupInfoList]
    prodTrafficRoute: Optional[TrafficRoute]
    testTrafficRoute: Optional[TrafficRoute]


TargetGroupPairInfoList = List[TargetGroupPairInfo]


class ELBInfo(TypedDict, total=False):
    name: Optional[ELBName]


ELBInfoList = List[ELBInfo]


class LoadBalancerInfo(TypedDict, total=False):
    elbInfoList: Optional[ELBInfoList]
    targetGroupInfoList: Optional[TargetGroupInfoList]
    targetGroupPairInfoList: Optional[TargetGroupPairInfoList]


class GreenFleetProvisioningOption(TypedDict, total=False):
    action: Optional[GreenFleetProvisioningAction]


class DeploymentReadyOption(TypedDict, total=False):
    actionOnTimeout: Optional[DeploymentReadyAction]
    waitTimeInMinutes: Optional[Duration]


class BlueInstanceTerminationOption(TypedDict, total=False):
    action: Optional[InstanceAction]
    terminationWaitTimeInMinutes: Optional[Duration]


class BlueGreenDeploymentConfiguration(TypedDict, total=False):
    terminateBlueInstancesOnDeploymentSuccess: Optional[BlueInstanceTerminationOption]
    deploymentReadyOption: Optional[DeploymentReadyOption]
    greenFleetProvisioningOption: Optional[GreenFleetProvisioningOption]


class DeploymentStyle(TypedDict, total=False):
    deploymentType: Optional[DeploymentType]
    deploymentOption: Optional[DeploymentOption]


TriggerEventTypeList = List[TriggerEventType]


class TriggerConfig(TypedDict, total=False):
    triggerName: Optional[TriggerName]
    triggerTargetArn: Optional[TriggerTargetArn]
    triggerEvents: Optional[TriggerEventTypeList]


TriggerConfigList = List[TriggerConfig]


class DeploymentGroupInfo(TypedDict, total=False):
    applicationName: Optional[ApplicationName]
    deploymentGroupId: Optional[DeploymentGroupId]
    deploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupList]
    serviceRoleArn: Optional[Role]
    targetRevision: Optional[RevisionLocation]
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    deploymentStyle: Optional[DeploymentStyle]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    lastSuccessfulDeployment: Optional[LastDeploymentInfo]
    lastAttemptedDeployment: Optional[LastDeploymentInfo]
    ec2TagSet: Optional[EC2TagSet]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    computePlatform: Optional[ComputePlatform]
    ecsServices: Optional[ECSServiceList]
    terminationHookEnabled: Optional[Boolean]


DeploymentGroupInfoList = List[DeploymentGroupInfo]


class BatchGetDeploymentGroupsOutput(TypedDict, total=False):
    deploymentGroupsInfo: Optional[DeploymentGroupInfoList]
    errorMessage: Optional[ErrorMessage]


InstancesList = List[InstanceId]


class BatchGetDeploymentInstancesInput(ServiceRequest):
    deploymentId: DeploymentId
    instanceIds: InstancesList


class Diagnostics(TypedDict, total=False):
    errorCode: Optional[LifecycleErrorCode]
    scriptName: Optional[ScriptName]
    message: Optional[LifecycleMessage]
    logTail: Optional[LogTail]


class LifecycleEvent(TypedDict, total=False):
    lifecycleEventName: Optional[LifecycleEventName]
    diagnostics: Optional[Diagnostics]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    status: Optional[LifecycleEventStatus]


LifecycleEventList = List[LifecycleEvent]


class InstanceSummary(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    instanceId: Optional[InstanceId]
    status: Optional[InstanceStatus]
    lastUpdatedAt: Optional[Timestamp]
    lifecycleEvents: Optional[LifecycleEventList]
    instanceType: Optional[InstanceType]


InstanceSummaryList = List[InstanceSummary]


class BatchGetDeploymentInstancesOutput(TypedDict, total=False):
    instancesSummary: Optional[InstanceSummaryList]
    errorMessage: Optional[ErrorMessage]


TargetIdList = List[TargetId]


class BatchGetDeploymentTargetsInput(ServiceRequest):
    deploymentId: DeploymentId
    targetIds: TargetIdList


Time = datetime


class CloudFormationTarget(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    status: Optional[TargetStatus]
    resourceType: Optional[CloudFormationResourceType]
    targetVersionWeight: Optional[TrafficWeight]


ECSTaskSetCount = int


class ECSTaskSet(TypedDict, total=False):
    identifer: Optional[ECSTaskSetIdentifier]
    desiredCount: Optional[ECSTaskSetCount]
    pendingCount: Optional[ECSTaskSetCount]
    runningCount: Optional[ECSTaskSetCount]
    status: Optional[ECSTaskSetStatus]
    trafficWeight: Optional[TrafficWeight]
    targetGroup: Optional[TargetGroupInfo]
    taskSetLabel: Optional[TargetLabel]


ECSTaskSetList = List[ECSTaskSet]


class ECSTarget(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    status: Optional[TargetStatus]
    taskSetsInfo: Optional[ECSTaskSetList]


class LambdaFunctionInfo(TypedDict, total=False):
    functionName: Optional[LambdaFunctionName]
    functionAlias: Optional[LambdaFunctionAlias]
    currentVersion: Optional[Version]
    targetVersion: Optional[Version]
    targetVersionWeight: Optional[TrafficWeight]


class LambdaTarget(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    status: Optional[TargetStatus]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    lambdaFunctionInfo: Optional[LambdaFunctionInfo]


class InstanceTarget(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    status: Optional[TargetStatus]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    instanceLabel: Optional[TargetLabel]


class DeploymentTarget(TypedDict, total=False):
    deploymentTargetType: Optional[DeploymentTargetType]
    instanceTarget: Optional[InstanceTarget]
    lambdaTarget: Optional[LambdaTarget]
    ecsTarget: Optional[ECSTarget]
    cloudFormationTarget: Optional[CloudFormationTarget]


DeploymentTargetList = List[DeploymentTarget]


class BatchGetDeploymentTargetsOutput(TypedDict, total=False):
    deploymentTargets: Optional[DeploymentTargetList]


DeploymentsList = List[DeploymentId]


class BatchGetDeploymentsInput(ServiceRequest):
    deploymentIds: DeploymentsList


class RelatedDeployments(TypedDict, total=False):
    autoUpdateOutdatedInstancesRootDeploymentId: Optional[DeploymentId]
    autoUpdateOutdatedInstancesDeploymentIds: Optional[DeploymentsList]


DeploymentStatusMessageList = List[ErrorMessage]


class TargetInstances(TypedDict, total=False):
    tagFilters: Optional[EC2TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    ec2TagSet: Optional[EC2TagSet]


class RollbackInfo(TypedDict, total=False):
    rollbackDeploymentId: Optional[DeploymentId]
    rollbackTriggeringDeploymentId: Optional[DeploymentId]
    rollbackMessage: Optional[Description]


InstanceCount = int


class DeploymentOverview(TypedDict, total=False):
    Pending: Optional[InstanceCount]
    InProgress: Optional[InstanceCount]
    Succeeded: Optional[InstanceCount]
    Failed: Optional[InstanceCount]
    Skipped: Optional[InstanceCount]
    Ready: Optional[InstanceCount]


class ErrorInformation(TypedDict, total=False):
    code: Optional[ErrorCode]
    message: Optional[ErrorMessage]


class DeploymentInfo(TypedDict, total=False):
    applicationName: Optional[ApplicationName]
    deploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    deploymentId: Optional[DeploymentId]
    previousRevision: Optional[RevisionLocation]
    revision: Optional[RevisionLocation]
    status: Optional[DeploymentStatus]
    errorInformation: Optional[ErrorInformation]
    createTime: Optional[Timestamp]
    startTime: Optional[Timestamp]
    completeTime: Optional[Timestamp]
    deploymentOverview: Optional[DeploymentOverview]
    description: Optional[Description]
    creator: Optional[DeploymentCreator]
    ignoreApplicationStopFailures: Optional[Boolean]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    updateOutdatedInstancesOnly: Optional[Boolean]
    rollbackInfo: Optional[RollbackInfo]
    deploymentStyle: Optional[DeploymentStyle]
    targetInstances: Optional[TargetInstances]
    instanceTerminationWaitTimeStarted: Optional[Boolean]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    additionalDeploymentStatusInfo: Optional[AdditionalDeploymentStatusInfo]
    fileExistsBehavior: Optional[FileExistsBehavior]
    deploymentStatusMessages: Optional[DeploymentStatusMessageList]
    computePlatform: Optional[ComputePlatform]
    externalId: Optional[ExternalId]
    relatedDeployments: Optional[RelatedDeployments]
    overrideAlarmConfiguration: Optional[AlarmConfiguration]


DeploymentsInfoList = List[DeploymentInfo]


class BatchGetDeploymentsOutput(TypedDict, total=False):
    deploymentsInfo: Optional[DeploymentsInfoList]


class BatchGetOnPremisesInstancesInput(ServiceRequest):
    instanceNames: InstanceNameList


class InstanceInfo(TypedDict, total=False):
    instanceName: Optional[InstanceName]
    iamSessionArn: Optional[IamSessionArn]
    iamUserArn: Optional[IamUserArn]
    instanceArn: Optional[InstanceArn]
    registerTime: Optional[Timestamp]
    deregisterTime: Optional[Timestamp]
    tags: Optional[TagList]


InstanceInfoList = List[InstanceInfo]


class BatchGetOnPremisesInstancesOutput(TypedDict, total=False):
    instanceInfos: Optional[InstanceInfoList]


class ContinueDeploymentInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]
    deploymentWaitType: Optional[DeploymentWaitType]


class CreateApplicationInput(ServiceRequest):
    applicationName: ApplicationName
    computePlatform: Optional[ComputePlatform]
    tags: Optional[TagList]


class CreateApplicationOutput(TypedDict, total=False):
    applicationId: Optional[ApplicationId]


MinimumHealthyHostsPerZone = TypedDict(
    "MinimumHealthyHostsPerZone",
    {
        "type": Optional[MinimumHealthyHostsPerZoneType],
        "value": Optional[MinimumHealthyHostsPerZoneValue],
    },
    total=False,
)
WaitTimeInSeconds = int


class ZonalConfig(TypedDict, total=False):
    firstZoneMonitorDurationInSeconds: Optional[WaitTimeInSeconds]
    monitorDurationInSeconds: Optional[WaitTimeInSeconds]
    minimumHealthyHostsPerZone: Optional[MinimumHealthyHostsPerZone]


class TimeBasedLinear(TypedDict, total=False):
    linearPercentage: Optional[Percentage]
    linearInterval: Optional[WaitTimeInMins]


class TimeBasedCanary(TypedDict, total=False):
    canaryPercentage: Optional[Percentage]
    canaryInterval: Optional[WaitTimeInMins]


TrafficRoutingConfig = TypedDict(
    "TrafficRoutingConfig",
    {
        "type": Optional[TrafficRoutingType],
        "timeBasedCanary": Optional[TimeBasedCanary],
        "timeBasedLinear": Optional[TimeBasedLinear],
    },
    total=False,
)
MinimumHealthyHosts = TypedDict(
    "MinimumHealthyHosts",
    {
        "type": Optional[MinimumHealthyHostsType],
        "value": Optional[MinimumHealthyHostsValue],
    },
    total=False,
)


class CreateDeploymentConfigInput(ServiceRequest):
    deploymentConfigName: DeploymentConfigName
    minimumHealthyHosts: Optional[MinimumHealthyHosts]
    trafficRoutingConfig: Optional[TrafficRoutingConfig]
    computePlatform: Optional[ComputePlatform]
    zonalConfig: Optional[ZonalConfig]


class CreateDeploymentConfigOutput(TypedDict, total=False):
    deploymentConfigId: Optional[DeploymentConfigId]


class CreateDeploymentGroupInput(ServiceRequest):
    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    serviceRoleArn: Role
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    deploymentStyle: Optional[DeploymentStyle]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    ec2TagSet: Optional[EC2TagSet]
    ecsServices: Optional[ECSServiceList]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    tags: Optional[TagList]
    terminationHookEnabled: Optional[NullableBoolean]


class CreateDeploymentGroupOutput(TypedDict, total=False):
    deploymentGroupId: Optional[DeploymentGroupId]


class CreateDeploymentInput(ServiceRequest):
    applicationName: ApplicationName
    deploymentGroupName: Optional[DeploymentGroupName]
    revision: Optional[RevisionLocation]
    deploymentConfigName: Optional[DeploymentConfigName]
    description: Optional[Description]
    ignoreApplicationStopFailures: Optional[Boolean]
    targetInstances: Optional[TargetInstances]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    updateOutdatedInstancesOnly: Optional[Boolean]
    fileExistsBehavior: Optional[FileExistsBehavior]
    overrideAlarmConfiguration: Optional[AlarmConfiguration]


class CreateDeploymentOutput(TypedDict, total=False):
    deploymentId: Optional[DeploymentId]


class DeleteApplicationInput(ServiceRequest):
    applicationName: ApplicationName


class DeleteDeploymentConfigInput(ServiceRequest):
    deploymentConfigName: DeploymentConfigName


class DeleteDeploymentGroupInput(ServiceRequest):
    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName


class DeleteDeploymentGroupOutput(TypedDict, total=False):
    hooksNotCleanedUp: Optional[AutoScalingGroupList]


class DeleteGitHubAccountTokenInput(ServiceRequest):
    tokenName: Optional[GitHubAccountTokenName]


class DeleteGitHubAccountTokenOutput(TypedDict, total=False):
    tokenName: Optional[GitHubAccountTokenName]


class DeleteResourcesByExternalIdInput(ServiceRequest):
    externalId: Optional[ExternalId]


class DeleteResourcesByExternalIdOutput(TypedDict, total=False):
    pass


class DeploymentConfigInfo(TypedDict, total=False):
    deploymentConfigId: Optional[DeploymentConfigId]
    deploymentConfigName: Optional[DeploymentConfigName]
    minimumHealthyHosts: Optional[MinimumHealthyHosts]
    createTime: Optional[Timestamp]
    computePlatform: Optional[ComputePlatform]
    trafficRoutingConfig: Optional[TrafficRoutingConfig]
    zonalConfig: Optional[ZonalConfig]


DeploymentConfigsList = List[DeploymentConfigName]
DeploymentStatusList = List[DeploymentStatus]


class DeregisterOnPremisesInstanceInput(ServiceRequest):
    instanceName: InstanceName


FilterValueList = List[FilterValue]


class GetApplicationInput(ServiceRequest):
    applicationName: ApplicationName


class GetApplicationOutput(TypedDict, total=False):
    application: Optional[ApplicationInfo]


class GetApplicationRevisionInput(ServiceRequest):
    applicationName: ApplicationName
    revision: RevisionLocation


class GetApplicationRevisionOutput(TypedDict, total=False):
    applicationName: Optional[ApplicationName]
    revision: Optional[RevisionLocation]
    revisionInfo: Optional[GenericRevisionInfo]


class GetDeploymentConfigInput(ServiceRequest):
    deploymentConfigName: DeploymentConfigName


class GetDeploymentConfigOutput(TypedDict, total=False):
    deploymentConfigInfo: Optional[DeploymentConfigInfo]


class GetDeploymentGroupInput(ServiceRequest):
    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName


class GetDeploymentGroupOutput(TypedDict, total=False):
    deploymentGroupInfo: Optional[DeploymentGroupInfo]


class GetDeploymentInput(ServiceRequest):
    deploymentId: DeploymentId


class GetDeploymentInstanceInput(ServiceRequest):
    deploymentId: DeploymentId
    instanceId: InstanceId


class GetDeploymentInstanceOutput(TypedDict, total=False):
    instanceSummary: Optional[InstanceSummary]


class GetDeploymentOutput(TypedDict, total=False):
    deploymentInfo: Optional[DeploymentInfo]


class GetDeploymentTargetInput(ServiceRequest):
    deploymentId: DeploymentId
    targetId: TargetId


class GetDeploymentTargetOutput(TypedDict, total=False):
    deploymentTarget: Optional[DeploymentTarget]


class GetOnPremisesInstanceInput(ServiceRequest):
    instanceName: InstanceName


class GetOnPremisesInstanceOutput(TypedDict, total=False):
    instanceInfo: Optional[InstanceInfo]


GitHubAccountTokenNameList = List[GitHubAccountTokenName]
InstanceStatusList = List[InstanceStatus]
InstanceTypeList = List[InstanceType]


class ListApplicationRevisionsInput(ServiceRequest):
    applicationName: ApplicationName
    sortBy: Optional[ApplicationRevisionSortBy]
    sortOrder: Optional[SortOrder]
    s3Bucket: Optional[S3Bucket]
    s3KeyPrefix: Optional[S3Key]
    deployed: Optional[ListStateFilterAction]
    nextToken: Optional[NextToken]


class ListApplicationRevisionsOutput(TypedDict, total=False):
    revisions: Optional[RevisionLocationList]
    nextToken: Optional[NextToken]


class ListApplicationsInput(ServiceRequest):
    nextToken: Optional[NextToken]


class ListApplicationsOutput(TypedDict, total=False):
    applications: Optional[ApplicationsList]
    nextToken: Optional[NextToken]


class ListDeploymentConfigsInput(ServiceRequest):
    nextToken: Optional[NextToken]


class ListDeploymentConfigsOutput(TypedDict, total=False):
    deploymentConfigsList: Optional[DeploymentConfigsList]
    nextToken: Optional[NextToken]


class ListDeploymentGroupsInput(ServiceRequest):
    applicationName: ApplicationName
    nextToken: Optional[NextToken]


class ListDeploymentGroupsOutput(TypedDict, total=False):
    applicationName: Optional[ApplicationName]
    deploymentGroups: Optional[DeploymentGroupsList]
    nextToken: Optional[NextToken]


class ListDeploymentInstancesInput(ServiceRequest):
    deploymentId: DeploymentId
    nextToken: Optional[NextToken]
    instanceStatusFilter: Optional[InstanceStatusList]
    instanceTypeFilter: Optional[InstanceTypeList]


class ListDeploymentInstancesOutput(TypedDict, total=False):
    instancesList: Optional[InstancesList]
    nextToken: Optional[NextToken]


TargetFilters = Dict[TargetFilterName, FilterValueList]


class ListDeploymentTargetsInput(ServiceRequest):
    deploymentId: DeploymentId
    nextToken: Optional[NextToken]
    targetFilters: Optional[TargetFilters]


class ListDeploymentTargetsOutput(TypedDict, total=False):
    targetIds: Optional[TargetIdList]
    nextToken: Optional[NextToken]


class TimeRange(TypedDict, total=False):
    start: Optional[Timestamp]
    end: Optional[Timestamp]


class ListDeploymentsInput(ServiceRequest):
    applicationName: Optional[ApplicationName]
    deploymentGroupName: Optional[DeploymentGroupName]
    externalId: Optional[ExternalId]
    includeOnlyStatuses: Optional[DeploymentStatusList]
    createTimeRange: Optional[TimeRange]
    nextToken: Optional[NextToken]


class ListDeploymentsOutput(TypedDict, total=False):
    deployments: Optional[DeploymentsList]
    nextToken: Optional[NextToken]


class ListGitHubAccountTokenNamesInput(ServiceRequest):
    nextToken: Optional[NextToken]


class ListGitHubAccountTokenNamesOutput(TypedDict, total=False):
    tokenNameList: Optional[GitHubAccountTokenNameList]
    nextToken: Optional[NextToken]


class ListOnPremisesInstancesInput(ServiceRequest):
    registrationStatus: Optional[RegistrationStatus]
    tagFilters: Optional[TagFilterList]
    nextToken: Optional[NextToken]


class ListOnPremisesInstancesOutput(TypedDict, total=False):
    instanceNames: Optional[InstanceNameList]
    nextToken: Optional[NextToken]


class ListTagsForResourceInput(ServiceRequest):
    ResourceArn: Arn
    NextToken: Optional[NextToken]


class ListTagsForResourceOutput(TypedDict, total=False):
    Tags: Optional[TagList]
    NextToken: Optional[NextToken]


class PutLifecycleEventHookExecutionStatusInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]
    lifecycleEventHookExecutionId: Optional[LifecycleEventHookExecutionId]
    status: Optional[LifecycleEventStatus]


class PutLifecycleEventHookExecutionStatusOutput(TypedDict, total=False):
    lifecycleEventHookExecutionId: Optional[LifecycleEventHookExecutionId]


class RegisterApplicationRevisionInput(ServiceRequest):
    applicationName: ApplicationName
    description: Optional[Description]
    revision: RevisionLocation


class RegisterOnPremisesInstanceInput(ServiceRequest):
    instanceName: InstanceName
    iamSessionArn: Optional[IamSessionArn]
    iamUserArn: Optional[IamUserArn]


class RemoveTagsFromOnPremisesInstancesInput(ServiceRequest):
    tags: TagList
    instanceNames: InstanceNameList


class SkipWaitTimeForInstanceTerminationInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]


class StopDeploymentInput(ServiceRequest):
    deploymentId: DeploymentId
    autoRollbackEnabled: Optional[NullableBoolean]


class StopDeploymentOutput(TypedDict, total=False):
    status: Optional[StopStatus]
    statusMessage: Optional[Message]


TagKeyList = List[Key]


class TagResourceInput(ServiceRequest):
    ResourceArn: Arn
    Tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    ResourceArn: Arn
    TagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateApplicationInput(ServiceRequest):
    applicationName: Optional[ApplicationName]
    newApplicationName: Optional[ApplicationName]


class UpdateDeploymentGroupInput(ServiceRequest):
    applicationName: ApplicationName
    currentDeploymentGroupName: DeploymentGroupName
    newDeploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    serviceRoleArn: Optional[Role]
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    deploymentStyle: Optional[DeploymentStyle]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    ec2TagSet: Optional[EC2TagSet]
    ecsServices: Optional[ECSServiceList]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    terminationHookEnabled: Optional[NullableBoolean]


class UpdateDeploymentGroupOutput(TypedDict, total=False):
    hooksNotCleanedUp: Optional[AutoScalingGroupList]


class CodedeployApi:
    service = "codedeploy"
    version = "2014-10-06"

    @handler("AddTagsToOnPremisesInstances")
    def add_tags_to_on_premises_instances(
        self, context: RequestContext, tags: TagList, instance_names: InstanceNameList, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("BatchGetApplicationRevisions")
    def batch_get_application_revisions(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revisions: RevisionLocationList,
        **kwargs,
    ) -> BatchGetApplicationRevisionsOutput:
        raise NotImplementedError

    @handler("BatchGetApplications")
    def batch_get_applications(
        self, context: RequestContext, application_names: ApplicationsList, **kwargs
    ) -> BatchGetApplicationsOutput:
        raise NotImplementedError

    @handler("BatchGetDeploymentGroups")
    def batch_get_deployment_groups(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_names: DeploymentGroupsList,
        **kwargs,
    ) -> BatchGetDeploymentGroupsOutput:
        raise NotImplementedError

    @handler("BatchGetDeploymentInstances")
    def batch_get_deployment_instances(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        instance_ids: InstancesList,
        **kwargs,
    ) -> BatchGetDeploymentInstancesOutput:
        raise NotImplementedError

    @handler("BatchGetDeploymentTargets")
    def batch_get_deployment_targets(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        target_ids: TargetIdList,
        **kwargs,
    ) -> BatchGetDeploymentTargetsOutput:
        raise NotImplementedError

    @handler("BatchGetDeployments")
    def batch_get_deployments(
        self, context: RequestContext, deployment_ids: DeploymentsList, **kwargs
    ) -> BatchGetDeploymentsOutput:
        raise NotImplementedError

    @handler("BatchGetOnPremisesInstances")
    def batch_get_on_premises_instances(
        self, context: RequestContext, instance_names: InstanceNameList, **kwargs
    ) -> BatchGetOnPremisesInstancesOutput:
        raise NotImplementedError

    @handler("ContinueDeployment")
    def continue_deployment(
        self,
        context: RequestContext,
        deployment_id: DeploymentId = None,
        deployment_wait_type: DeploymentWaitType = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("CreateApplication")
    def create_application(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        compute_platform: ComputePlatform = None,
        tags: TagList = None,
        **kwargs,
    ) -> CreateApplicationOutput:
        raise NotImplementedError

    @handler("CreateDeployment")
    def create_deployment(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName = None,
        revision: RevisionLocation = None,
        deployment_config_name: DeploymentConfigName = None,
        description: Description = None,
        ignore_application_stop_failures: Boolean = None,
        target_instances: TargetInstances = None,
        auto_rollback_configuration: AutoRollbackConfiguration = None,
        update_outdated_instances_only: Boolean = None,
        file_exists_behavior: FileExistsBehavior = None,
        override_alarm_configuration: AlarmConfiguration = None,
        **kwargs,
    ) -> CreateDeploymentOutput:
        raise NotImplementedError

    @handler("CreateDeploymentConfig")
    def create_deployment_config(
        self,
        context: RequestContext,
        deployment_config_name: DeploymentConfigName,
        minimum_healthy_hosts: MinimumHealthyHosts = None,
        traffic_routing_config: TrafficRoutingConfig = None,
        compute_platform: ComputePlatform = None,
        zonal_config: ZonalConfig = None,
        **kwargs,
    ) -> CreateDeploymentConfigOutput:
        raise NotImplementedError

    @handler("CreateDeploymentGroup")
    def create_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        service_role_arn: Role,
        deployment_config_name: DeploymentConfigName = None,
        ec2_tag_filters: EC2TagFilterList = None,
        on_premises_instance_tag_filters: TagFilterList = None,
        auto_scaling_groups: AutoScalingGroupNameList = None,
        trigger_configurations: TriggerConfigList = None,
        alarm_configuration: AlarmConfiguration = None,
        auto_rollback_configuration: AutoRollbackConfiguration = None,
        outdated_instances_strategy: OutdatedInstancesStrategy = None,
        deployment_style: DeploymentStyle = None,
        blue_green_deployment_configuration: BlueGreenDeploymentConfiguration = None,
        load_balancer_info: LoadBalancerInfo = None,
        ec2_tag_set: EC2TagSet = None,
        ecs_services: ECSServiceList = None,
        on_premises_tag_set: OnPremisesTagSet = None,
        tags: TagList = None,
        termination_hook_enabled: NullableBoolean = None,
        **kwargs,
    ) -> CreateDeploymentGroupOutput:
        raise NotImplementedError

    @handler("DeleteApplication")
    def delete_application(
        self, context: RequestContext, application_name: ApplicationName, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("DeleteDeploymentConfig")
    def delete_deployment_config(
        self, context: RequestContext, deployment_config_name: DeploymentConfigName, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("DeleteDeploymentGroup")
    def delete_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        **kwargs,
    ) -> DeleteDeploymentGroupOutput:
        raise NotImplementedError

    @handler("DeleteGitHubAccountToken")
    def delete_git_hub_account_token(
        self, context: RequestContext, token_name: GitHubAccountTokenName = None, **kwargs
    ) -> DeleteGitHubAccountTokenOutput:
        raise NotImplementedError

    @handler("DeleteResourcesByExternalId")
    def delete_resources_by_external_id(
        self, context: RequestContext, external_id: ExternalId = None, **kwargs
    ) -> DeleteResourcesByExternalIdOutput:
        raise NotImplementedError

    @handler("DeregisterOnPremisesInstance")
    def deregister_on_premises_instance(
        self, context: RequestContext, instance_name: InstanceName, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("GetApplication")
    def get_application(
        self, context: RequestContext, application_name: ApplicationName, **kwargs
    ) -> GetApplicationOutput:
        raise NotImplementedError

    @handler("GetApplicationRevision")
    def get_application_revision(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revision: RevisionLocation,
        **kwargs,
    ) -> GetApplicationRevisionOutput:
        raise NotImplementedError

    @handler("GetDeployment")
    def get_deployment(
        self, context: RequestContext, deployment_id: DeploymentId, **kwargs
    ) -> GetDeploymentOutput:
        raise NotImplementedError

    @handler("GetDeploymentConfig")
    def get_deployment_config(
        self, context: RequestContext, deployment_config_name: DeploymentConfigName, **kwargs
    ) -> GetDeploymentConfigOutput:
        raise NotImplementedError

    @handler("GetDeploymentGroup")
    def get_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        **kwargs,
    ) -> GetDeploymentGroupOutput:
        raise NotImplementedError

    @handler("GetDeploymentInstance")
    def get_deployment_instance(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        instance_id: InstanceId,
        **kwargs,
    ) -> GetDeploymentInstanceOutput:
        raise NotImplementedError

    @handler("GetDeploymentTarget")
    def get_deployment_target(
        self, context: RequestContext, deployment_id: DeploymentId, target_id: TargetId, **kwargs
    ) -> GetDeploymentTargetOutput:
        raise NotImplementedError

    @handler("GetOnPremisesInstance")
    def get_on_premises_instance(
        self, context: RequestContext, instance_name: InstanceName, **kwargs
    ) -> GetOnPremisesInstanceOutput:
        raise NotImplementedError

    @handler("ListApplicationRevisions")
    def list_application_revisions(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        sort_by: ApplicationRevisionSortBy = None,
        sort_order: SortOrder = None,
        s3_bucket: S3Bucket = None,
        s3_key_prefix: S3Key = None,
        deployed: ListStateFilterAction = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListApplicationRevisionsOutput:
        raise NotImplementedError

    @handler("ListApplications")
    def list_applications(
        self, context: RequestContext, next_token: NextToken = None, **kwargs
    ) -> ListApplicationsOutput:
        raise NotImplementedError

    @handler("ListDeploymentConfigs")
    def list_deployment_configs(
        self, context: RequestContext, next_token: NextToken = None, **kwargs
    ) -> ListDeploymentConfigsOutput:
        raise NotImplementedError

    @handler("ListDeploymentGroups")
    def list_deployment_groups(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListDeploymentGroupsOutput:
        raise NotImplementedError

    @handler("ListDeploymentInstances")
    def list_deployment_instances(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        next_token: NextToken = None,
        instance_status_filter: InstanceStatusList = None,
        instance_type_filter: InstanceTypeList = None,
        **kwargs,
    ) -> ListDeploymentInstancesOutput:
        raise NotImplementedError

    @handler("ListDeploymentTargets")
    def list_deployment_targets(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        next_token: NextToken = None,
        target_filters: TargetFilters = None,
        **kwargs,
    ) -> ListDeploymentTargetsOutput:
        raise NotImplementedError

    @handler("ListDeployments")
    def list_deployments(
        self,
        context: RequestContext,
        application_name: ApplicationName = None,
        deployment_group_name: DeploymentGroupName = None,
        external_id: ExternalId = None,
        include_only_statuses: DeploymentStatusList = None,
        create_time_range: TimeRange = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListDeploymentsOutput:
        raise NotImplementedError

    @handler("ListGitHubAccountTokenNames")
    def list_git_hub_account_token_names(
        self, context: RequestContext, next_token: NextToken = None, **kwargs
    ) -> ListGitHubAccountTokenNamesOutput:
        raise NotImplementedError

    @handler("ListOnPremisesInstances")
    def list_on_premises_instances(
        self,
        context: RequestContext,
        registration_status: RegistrationStatus = None,
        tag_filters: TagFilterList = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListOnPremisesInstancesOutput:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: Arn, next_token: NextToken = None, **kwargs
    ) -> ListTagsForResourceOutput:
        raise NotImplementedError

    @handler("PutLifecycleEventHookExecutionStatus")
    def put_lifecycle_event_hook_execution_status(
        self,
        context: RequestContext,
        deployment_id: DeploymentId = None,
        lifecycle_event_hook_execution_id: LifecycleEventHookExecutionId = None,
        status: LifecycleEventStatus = None,
        **kwargs,
    ) -> PutLifecycleEventHookExecutionStatusOutput:
        raise NotImplementedError

    @handler("RegisterApplicationRevision")
    def register_application_revision(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revision: RevisionLocation,
        description: Description = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("RegisterOnPremisesInstance")
    def register_on_premises_instance(
        self,
        context: RequestContext,
        instance_name: InstanceName,
        iam_session_arn: IamSessionArn = None,
        iam_user_arn: IamUserArn = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("RemoveTagsFromOnPremisesInstances")
    def remove_tags_from_on_premises_instances(
        self, context: RequestContext, tags: TagList, instance_names: InstanceNameList, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("SkipWaitTimeForInstanceTermination")
    def skip_wait_time_for_instance_termination(
        self, context: RequestContext, deployment_id: DeploymentId = None, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("StopDeployment")
    def stop_deployment(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        auto_rollback_enabled: NullableBoolean = None,
        **kwargs,
    ) -> StopDeploymentOutput:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: Arn, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: Arn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        raise NotImplementedError

    @handler("UpdateApplication")
    def update_application(
        self,
        context: RequestContext,
        application_name: ApplicationName = None,
        new_application_name: ApplicationName = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("UpdateDeploymentGroup")
    def update_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        current_deployment_group_name: DeploymentGroupName,
        new_deployment_group_name: DeploymentGroupName = None,
        deployment_config_name: DeploymentConfigName = None,
        ec2_tag_filters: EC2TagFilterList = None,
        on_premises_instance_tag_filters: TagFilterList = None,
        auto_scaling_groups: AutoScalingGroupNameList = None,
        service_role_arn: Role = None,
        trigger_configurations: TriggerConfigList = None,
        alarm_configuration: AlarmConfiguration = None,
        auto_rollback_configuration: AutoRollbackConfiguration = None,
        outdated_instances_strategy: OutdatedInstancesStrategy = None,
        deployment_style: DeploymentStyle = None,
        blue_green_deployment_configuration: BlueGreenDeploymentConfiguration = None,
        load_balancer_info: LoadBalancerInfo = None,
        ec2_tag_set: EC2TagSet = None,
        ecs_services: ECSServiceList = None,
        on_premises_tag_set: OnPremisesTagSet = None,
        termination_hook_enabled: NullableBoolean = None,
        **kwargs,
    ) -> UpdateDeploymentGroupOutput:
        raise NotImplementedError
