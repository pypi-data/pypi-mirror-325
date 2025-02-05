from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AWSRegionName = str
AccessKeyId = str
AccountId = str
ActionConfigurationKey = str
ActionConfigurationQueryableValue = str
ActionConfigurationValue = str
ActionExecutionId = str
ActionExecutionToken = str
ActionName = str
ActionNamespace = str
ActionProvider = str
ActionRunOrder = int
ActionTimeout = int
ActionTypeDescription = str
ActionTypeOwner = str
AllowedAccount = str
ApprovalSummary = str
ApprovalToken = str
ArtifactName = str
ArtifactStoreLocation = str
BlockerName = str
Boolean = bool
ClientId = str
ClientRequestToken = str
ClientToken = str
Code = str
Command = str
ContinuationToken = str
Description = str
DisabledReason = str
Enabled = bool
EncryptionKeyId = str
ExecutionId = str
ExecutionSummary = str
ExternalExecutionId = str
ExternalExecutionSummary = str
FilePath = str
GitBranchNamePattern = str
GitFilePathPattern = str
GitTagNamePattern = str
JobId = str
JobTimeout = int
JsonPath = str
LambdaFunctionArn = str
LastChangedBy = str
LastUpdatedBy = str
LogStreamARN = str
MatchEquals = str
MaxBatchSize = int
MaxPipelines = int
MaxResults = int
MaximumActionTypeArtifactCount = int
MaximumArtifactCount = int
Message = str
MinimumActionTypeArtifactCount = int
MinimumArtifactCount = int
NextToken = str
Nonce = str
OutputVariable = str
OutputVariablesKey = str
OutputVariablesValue = str
Percentage = int
PipelineArn = str
PipelineExecutionId = str
PipelineExecutionStatusSummary = str
PipelineName = str
PipelineVariableDescription = str
PipelineVariableName = str
PipelineVariableValue = str
PipelineVersion = int
PolicyStatementsTemplate = str
PropertyDescription = str
ResourceArn = str
RetryAttempt = int
Revision = str
RevisionChangeIdentifier = str
RevisionSummary = str
RoleArn = str
RuleConfigurationKey = str
RuleConfigurationValue = str
RuleExecutionId = str
RuleExecutionToken = str
RuleName = str
RuleProvider = str
RuleTimeout = int
S3Bucket = str
S3BucketName = str
S3Key = str
S3ObjectKey = str
SecretAccessKey = str
ServicePrincipal = str
SessionToken = str
StageName = str
StopPipelineExecutionReason = str
String = str
TagKey = str
TagValue = str
ThirdPartyJobId = str
TriggerDetail = str
Url = str
UrlTemplate = str
Version = str
WebhookArn = str
WebhookAuthConfigurationAllowedIPRange = str
WebhookAuthConfigurationSecretToken = str
WebhookErrorCode = str
WebhookErrorMessage = str
WebhookName = str
WebhookUrl = str


class ActionCategory(StrEnum):
    Source = "Source"
    Build = "Build"
    Deploy = "Deploy"
    Test = "Test"
    Invoke = "Invoke"
    Approval = "Approval"
    Compute = "Compute"


class ActionConfigurationPropertyType(StrEnum):
    String = "String"
    Number = "Number"
    Boolean = "Boolean"


class ActionExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Abandoned = "Abandoned"
    Succeeded = "Succeeded"
    Failed = "Failed"


class ActionOwner(StrEnum):
    AWS = "AWS"
    ThirdParty = "ThirdParty"
    Custom = "Custom"


class ApprovalStatus(StrEnum):
    Approved = "Approved"
    Rejected = "Rejected"


class ArtifactLocationType(StrEnum):
    S3 = "S3"


class ArtifactStoreType(StrEnum):
    S3 = "S3"


class BlockerType(StrEnum):
    Schedule = "Schedule"


class ConditionExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Failed = "Failed"
    Errored = "Errored"
    Succeeded = "Succeeded"
    Cancelled = "Cancelled"
    Abandoned = "Abandoned"
    Overridden = "Overridden"


class ConditionType(StrEnum):
    BEFORE_ENTRY = "BEFORE_ENTRY"
    ON_SUCCESS = "ON_SUCCESS"


class EncryptionKeyType(StrEnum):
    KMS = "KMS"


class ExecutionMode(StrEnum):
    QUEUED = "QUEUED"
    SUPERSEDED = "SUPERSEDED"
    PARALLEL = "PARALLEL"


class ExecutionType(StrEnum):
    STANDARD = "STANDARD"
    ROLLBACK = "ROLLBACK"


class ExecutorType(StrEnum):
    JobWorker = "JobWorker"
    Lambda = "Lambda"


class FailureType(StrEnum):
    JobFailed = "JobFailed"
    ConfigurationError = "ConfigurationError"
    PermissionError = "PermissionError"
    RevisionOutOfSync = "RevisionOutOfSync"
    RevisionUnavailable = "RevisionUnavailable"
    SystemUnavailable = "SystemUnavailable"


class GitPullRequestEventType(StrEnum):
    OPEN = "OPEN"
    UPDATED = "UPDATED"
    CLOSED = "CLOSED"


class JobStatus(StrEnum):
    Created = "Created"
    Queued = "Queued"
    Dispatched = "Dispatched"
    InProgress = "InProgress"
    TimedOut = "TimedOut"
    Succeeded = "Succeeded"
    Failed = "Failed"


class PipelineExecutionStatus(StrEnum):
    Cancelled = "Cancelled"
    InProgress = "InProgress"
    Stopped = "Stopped"
    Stopping = "Stopping"
    Succeeded = "Succeeded"
    Superseded = "Superseded"
    Failed = "Failed"


class PipelineTriggerProviderType(StrEnum):
    CodeStarSourceConnection = "CodeStarSourceConnection"


class PipelineType(StrEnum):
    V1 = "V1"
    V2 = "V2"


class Result(StrEnum):
    ROLLBACK = "ROLLBACK"
    FAIL = "FAIL"
    RETRY = "RETRY"
    SKIP = "SKIP"


class RetryTrigger(StrEnum):
    AutomatedStageRetry = "AutomatedStageRetry"
    ManualStageRetry = "ManualStageRetry"


class RuleCategory(StrEnum):
    Rule = "Rule"


class RuleConfigurationPropertyType(StrEnum):
    String = "String"
    Number = "Number"
    Boolean = "Boolean"


class RuleExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Abandoned = "Abandoned"
    Succeeded = "Succeeded"
    Failed = "Failed"


class RuleOwner(StrEnum):
    AWS = "AWS"


class SourceRevisionType(StrEnum):
    COMMIT_ID = "COMMIT_ID"
    IMAGE_DIGEST = "IMAGE_DIGEST"
    S3_OBJECT_VERSION_ID = "S3_OBJECT_VERSION_ID"
    S3_OBJECT_KEY = "S3_OBJECT_KEY"


class StageExecutionStatus(StrEnum):
    Cancelled = "Cancelled"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"
    Succeeded = "Succeeded"
    Skipped = "Skipped"


class StageRetryMode(StrEnum):
    FAILED_ACTIONS = "FAILED_ACTIONS"
    ALL_ACTIONS = "ALL_ACTIONS"


class StageTransitionType(StrEnum):
    Inbound = "Inbound"
    Outbound = "Outbound"


class StartTimeRange(StrEnum):
    Latest = "Latest"
    All = "All"


class TriggerType(StrEnum):
    CreatePipeline = "CreatePipeline"
    StartPipelineExecution = "StartPipelineExecution"
    PollForSourceChanges = "PollForSourceChanges"
    Webhook = "Webhook"
    CloudWatchEvent = "CloudWatchEvent"
    PutActionRevision = "PutActionRevision"
    WebhookV2 = "WebhookV2"
    ManualRollback = "ManualRollback"
    AutomatedRollback = "AutomatedRollback"


class WebhookAuthenticationType(StrEnum):
    GITHUB_HMAC = "GITHUB_HMAC"
    IP = "IP"
    UNAUTHENTICATED = "UNAUTHENTICATED"


class ActionNotFoundException(ServiceException):
    code: str = "ActionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ActionTypeAlreadyExistsException(ServiceException):
    code: str = "ActionTypeAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ActionTypeNotFoundException(ServiceException):
    code: str = "ActionTypeNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ApprovalAlreadyCompletedException(ServiceException):
    code: str = "ApprovalAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentPipelineExecutionsLimitExceededException(ServiceException):
    code: str = "ConcurrentPipelineExecutionsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ConditionNotOverridableException(ServiceException):
    code: str = "ConditionNotOverridableException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class DuplicatedStopRequestException(ServiceException):
    code: str = "DuplicatedStopRequestException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidActionDeclarationException(ServiceException):
    code: str = "InvalidActionDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidApprovalTokenException(ServiceException):
    code: str = "InvalidApprovalTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidArnException(ServiceException):
    code: str = "InvalidArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBlockerDeclarationException(ServiceException):
    code: str = "InvalidBlockerDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidClientTokenException(ServiceException):
    code: str = "InvalidClientTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidJobException(ServiceException):
    code: str = "InvalidJobException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidJobStateException(ServiceException):
    code: str = "InvalidJobStateException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNonceException(ServiceException):
    code: str = "InvalidNonceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStageDeclarationException(ServiceException):
    code: str = "InvalidStageDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStructureException(ServiceException):
    code: str = "InvalidStructureException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagsException(ServiceException):
    code: str = "InvalidTagsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidWebhookAuthenticationParametersException(ServiceException):
    code: str = "InvalidWebhookAuthenticationParametersException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidWebhookFilterPatternException(ServiceException):
    code: str = "InvalidWebhookFilterPatternException"
    sender_fault: bool = False
    status_code: int = 400


class JobNotFoundException(ServiceException):
    code: str = "JobNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class LimitExceededException(ServiceException):
    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class NotLatestPipelineExecutionException(ServiceException):
    code: str = "NotLatestPipelineExecutionException"
    sender_fault: bool = False
    status_code: int = 400


class OutputVariablesSizeExceededException(ServiceException):
    code: str = "OutputVariablesSizeExceededException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionNotFoundException(ServiceException):
    code: str = "PipelineExecutionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionNotStoppableException(ServiceException):
    code: str = "PipelineExecutionNotStoppableException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionOutdatedException(ServiceException):
    code: str = "PipelineExecutionOutdatedException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineNameInUseException(ServiceException):
    code: str = "PipelineNameInUseException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineNotFoundException(ServiceException):
    code: str = "PipelineNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineVersionNotFoundException(ServiceException):
    code: str = "PipelineVersionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class RequestFailedException(ServiceException):
    code: str = "RequestFailedException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class StageNotFoundException(ServiceException):
    code: str = "StageNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class StageNotRetryableException(ServiceException):
    code: str = "StageNotRetryableException"
    sender_fault: bool = False
    status_code: int = 400


class TooManyTagsException(ServiceException):
    code: str = "TooManyTagsException"
    sender_fault: bool = False
    status_code: int = 400


class UnableToRollbackStageException(ServiceException):
    code: str = "UnableToRollbackStageException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationException(ServiceException):
    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400


class WebhookNotFoundException(ServiceException):
    code: str = "WebhookNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class AWSSessionCredentials(TypedDict, total=False):
    accessKeyId: AccessKeyId
    secretAccessKey: SecretAccessKey
    sessionToken: SessionToken


class AcknowledgeJobInput(ServiceRequest):
    jobId: JobId
    nonce: Nonce


class AcknowledgeJobOutput(TypedDict, total=False):
    status: Optional[JobStatus]


class AcknowledgeThirdPartyJobInput(ServiceRequest):
    jobId: ThirdPartyJobId
    nonce: Nonce
    clientToken: ClientToken


class AcknowledgeThirdPartyJobOutput(TypedDict, total=False):
    status: Optional[JobStatus]


ActionConfigurationMap = Dict[ActionConfigurationKey, ActionConfigurationValue]


class ActionConfiguration(TypedDict, total=False):
    configuration: Optional[ActionConfigurationMap]


ActionConfigurationProperty = TypedDict(
    "ActionConfigurationProperty",
    {
        "name": ActionConfigurationKey,
        "required": Boolean,
        "key": Boolean,
        "secret": Boolean,
        "queryable": Optional[Boolean],
        "description": Optional[Description],
        "type": Optional[ActionConfigurationPropertyType],
    },
    total=False,
)
ActionConfigurationPropertyList = List[ActionConfigurationProperty]


class ActionContext(TypedDict, total=False):
    name: Optional[ActionName]
    actionExecutionId: Optional[ActionExecutionId]


OutputVariableList = List[OutputVariable]


class InputArtifact(TypedDict, total=False):
    name: ArtifactName


InputArtifactList = List[InputArtifact]
FilePathList = List[FilePath]


class OutputArtifact(TypedDict, total=False):
    name: ArtifactName
    files: Optional[FilePathList]


OutputArtifactList = List[OutputArtifact]
CommandList = List[Command]


class ActionTypeId(TypedDict, total=False):
    category: ActionCategory
    owner: ActionOwner
    provider: ActionProvider
    version: Version


class ActionDeclaration(TypedDict, total=False):
    name: ActionName
    actionTypeId: ActionTypeId
    runOrder: Optional[ActionRunOrder]
    configuration: Optional[ActionConfigurationMap]
    commands: Optional[CommandList]
    outputArtifacts: Optional[OutputArtifactList]
    inputArtifacts: Optional[InputArtifactList]
    outputVariables: Optional[OutputVariableList]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    namespace: Optional[ActionNamespace]
    timeoutInMinutes: Optional[ActionTimeout]


class ErrorDetails(TypedDict, total=False):
    code: Optional[Code]
    message: Optional[Message]


Timestamp = datetime


class ActionExecution(TypedDict, total=False):
    actionExecutionId: Optional[ActionExecutionId]
    status: Optional[ActionExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]
    token: Optional[ActionExecutionToken]
    lastUpdatedBy: Optional[LastUpdatedBy]
    externalExecutionId: Optional[ExecutionId]
    externalExecutionUrl: Optional[Url]
    percentComplete: Optional[Percentage]
    errorDetails: Optional[ErrorDetails]
    logStreamARN: Optional[LogStreamARN]


OutputVariablesMap = Dict[OutputVariablesKey, OutputVariablesValue]


class ActionExecutionResult(TypedDict, total=False):
    externalExecutionId: Optional[ExternalExecutionId]
    externalExecutionSummary: Optional[ExternalExecutionSummary]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]
    logStreamARN: Optional[LogStreamARN]


class S3Location(TypedDict, total=False):
    bucket: Optional[S3Bucket]
    key: Optional[S3Key]


class ArtifactDetail(TypedDict, total=False):
    name: Optional[ArtifactName]
    s3location: Optional[S3Location]


ArtifactDetailList = List[ArtifactDetail]


class ActionExecutionOutput(TypedDict, total=False):
    outputArtifacts: Optional[ArtifactDetailList]
    executionResult: Optional[ActionExecutionResult]
    outputVariables: Optional[OutputVariablesMap]


ResolvedActionConfigurationMap = Dict[String, String]


class ActionExecutionInput(TypedDict, total=False):
    actionTypeId: Optional[ActionTypeId]
    configuration: Optional[ActionConfigurationMap]
    resolvedConfiguration: Optional[ResolvedActionConfigurationMap]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    inputArtifacts: Optional[ArtifactDetailList]
    namespace: Optional[ActionNamespace]


class ActionExecutionDetail(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]
    actionExecutionId: Optional[ActionExecutionId]
    pipelineVersion: Optional[PipelineVersion]
    stageName: Optional[StageName]
    actionName: Optional[ActionName]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    updatedBy: Optional[LastUpdatedBy]
    status: Optional[ActionExecutionStatus]
    input: Optional[ActionExecutionInput]
    output: Optional[ActionExecutionOutput]


ActionExecutionDetailList = List[ActionExecutionDetail]


class LatestInPipelineExecutionFilter(TypedDict, total=False):
    pipelineExecutionId: PipelineExecutionId
    startTimeRange: StartTimeRange


class ActionExecutionFilter(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter]


class ActionRevision(TypedDict, total=False):
    revisionId: Revision
    revisionChangeId: RevisionChangeIdentifier
    created: Timestamp


class ActionState(TypedDict, total=False):
    actionName: Optional[ActionName]
    currentRevision: Optional[ActionRevision]
    latestExecution: Optional[ActionExecution]
    entityUrl: Optional[Url]
    revisionUrl: Optional[Url]


ActionStateList = List[ActionState]


class ArtifactDetails(TypedDict, total=False):
    minimumCount: MinimumArtifactCount
    maximumCount: MaximumArtifactCount


class ActionTypeSettings(TypedDict, total=False):
    thirdPartyConfigurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class ActionType(TypedDict, total=False):
    id: ActionTypeId
    settings: Optional[ActionTypeSettings]
    actionConfigurationProperties: Optional[ActionConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails


class ActionTypeArtifactDetails(TypedDict, total=False):
    minimumCount: MinimumActionTypeArtifactCount
    maximumCount: MaximumActionTypeArtifactCount


class ActionTypeUrls(TypedDict, total=False):
    configurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class ActionTypeProperty(TypedDict, total=False):
    name: ActionConfigurationKey
    optional: Boolean
    key: Boolean
    noEcho: Boolean
    queryable: Optional[Boolean]
    description: Optional[PropertyDescription]


ActionTypeProperties = List[ActionTypeProperty]
AllowedAccounts = List[AllowedAccount]


class ActionTypePermissions(TypedDict, total=False):
    allowedAccounts: AllowedAccounts


class ActionTypeIdentifier(TypedDict, total=False):
    category: ActionCategory
    owner: ActionTypeOwner
    provider: ActionProvider
    version: Version


PollingServicePrincipalList = List[ServicePrincipal]
PollingAccountList = List[AccountId]


class JobWorkerExecutorConfiguration(TypedDict, total=False):
    pollingAccounts: Optional[PollingAccountList]
    pollingServicePrincipals: Optional[PollingServicePrincipalList]


class LambdaExecutorConfiguration(TypedDict, total=False):
    lambdaFunctionArn: LambdaFunctionArn


class ExecutorConfiguration(TypedDict, total=False):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration]
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfiguration]


ActionTypeExecutor = TypedDict(
    "ActionTypeExecutor",
    {
        "configuration": ExecutorConfiguration,
        "type": ExecutorType,
        "policyStatementsTemplate": Optional[PolicyStatementsTemplate],
        "jobTimeout": Optional[JobTimeout],
    },
    total=False,
)


class ActionTypeDeclaration(TypedDict, total=False):
    description: Optional[ActionTypeDescription]
    executor: ActionTypeExecutor
    id: ActionTypeIdentifier
    inputArtifactDetails: ActionTypeArtifactDetails
    outputArtifactDetails: ActionTypeArtifactDetails
    permissions: Optional[ActionTypePermissions]
    properties: Optional[ActionTypeProperties]
    urls: Optional[ActionTypeUrls]


ActionTypeList = List[ActionType]


class ApprovalResult(TypedDict, total=False):
    summary: ApprovalSummary
    status: ApprovalStatus


class S3ArtifactLocation(TypedDict, total=False):
    bucketName: S3BucketName
    objectKey: S3ObjectKey


ArtifactLocation = TypedDict(
    "ArtifactLocation",
    {
        "type": Optional[ArtifactLocationType],
        "s3Location": Optional[S3ArtifactLocation],
    },
    total=False,
)


class Artifact(TypedDict, total=False):
    name: Optional[ArtifactName]
    revision: Optional[Revision]
    location: Optional[ArtifactLocation]


ArtifactList = List[Artifact]


class ArtifactRevision(TypedDict, total=False):
    name: Optional[ArtifactName]
    revisionId: Optional[Revision]
    revisionChangeIdentifier: Optional[RevisionChangeIdentifier]
    revisionSummary: Optional[RevisionSummary]
    created: Optional[Timestamp]
    revisionUrl: Optional[Url]


ArtifactRevisionList = List[ArtifactRevision]
EncryptionKey = TypedDict(
    "EncryptionKey",
    {
        "id": EncryptionKeyId,
        "type": EncryptionKeyType,
    },
    total=False,
)
ArtifactStore = TypedDict(
    "ArtifactStore",
    {
        "type": ArtifactStoreType,
        "location": ArtifactStoreLocation,
        "encryptionKey": Optional[EncryptionKey],
    },
    total=False,
)
ArtifactStoreMap = Dict[AWSRegionName, ArtifactStore]
RuleConfigurationMap = Dict[RuleConfigurationKey, RuleConfigurationValue]


class RuleTypeId(TypedDict, total=False):
    category: RuleCategory
    owner: Optional[RuleOwner]
    provider: RuleProvider
    version: Optional[Version]


class RuleDeclaration(TypedDict, total=False):
    name: RuleName
    ruleTypeId: RuleTypeId
    configuration: Optional[RuleConfigurationMap]
    commands: Optional[CommandList]
    inputArtifacts: Optional[InputArtifactList]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    timeoutInMinutes: Optional[RuleTimeout]


RuleDeclarationList = List[RuleDeclaration]


class Condition(TypedDict, total=False):
    result: Optional[Result]
    rules: Optional[RuleDeclarationList]


ConditionList = List[Condition]


class BeforeEntryConditions(TypedDict, total=False):
    conditions: ConditionList


BlockerDeclaration = TypedDict(
    "BlockerDeclaration",
    {
        "name": BlockerName,
        "type": BlockerType,
    },
    total=False,
)


class ConditionExecution(TypedDict, total=False):
    status: Optional[ConditionExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]


class RuleExecution(TypedDict, total=False):
    ruleExecutionId: Optional[RuleExecutionId]
    status: Optional[RuleExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]
    token: Optional[RuleExecutionToken]
    lastUpdatedBy: Optional[LastUpdatedBy]
    externalExecutionId: Optional[ExecutionId]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]


class RuleRevision(TypedDict, total=False):
    revisionId: Revision
    revisionChangeId: RevisionChangeIdentifier
    created: Timestamp


class RuleState(TypedDict, total=False):
    ruleName: Optional[RuleName]
    currentRevision: Optional[RuleRevision]
    latestExecution: Optional[RuleExecution]
    entityUrl: Optional[Url]
    revisionUrl: Optional[Url]


RuleStateList = List[RuleState]


class ConditionState(TypedDict, total=False):
    latestExecution: Optional[ConditionExecution]
    ruleStates: Optional[RuleStateList]


ConditionStateList = List[ConditionState]


class Tag(TypedDict, total=False):
    key: TagKey
    value: TagValue


TagList = List[Tag]


class CreateCustomActionTypeInput(ServiceRequest):
    category: ActionCategory
    provider: ActionProvider
    version: Version
    settings: Optional[ActionTypeSettings]
    configurationProperties: Optional[ActionConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails
    tags: Optional[TagList]


class CreateCustomActionTypeOutput(TypedDict, total=False):
    actionType: ActionType
    tags: Optional[TagList]


GitFilePathPatternList = List[GitFilePathPattern]


class GitFilePathFilterCriteria(TypedDict, total=False):
    includes: Optional[GitFilePathPatternList]
    excludes: Optional[GitFilePathPatternList]


GitBranchPatternList = List[GitBranchNamePattern]


class GitBranchFilterCriteria(TypedDict, total=False):
    includes: Optional[GitBranchPatternList]
    excludes: Optional[GitBranchPatternList]


GitPullRequestEventTypeList = List[GitPullRequestEventType]


class GitPullRequestFilter(TypedDict, total=False):
    events: Optional[GitPullRequestEventTypeList]
    branches: Optional[GitBranchFilterCriteria]
    filePaths: Optional[GitFilePathFilterCriteria]


GitPullRequestFilterList = List[GitPullRequestFilter]
GitTagPatternList = List[GitTagNamePattern]


class GitTagFilterCriteria(TypedDict, total=False):
    includes: Optional[GitTagPatternList]
    excludes: Optional[GitTagPatternList]


class GitPushFilter(TypedDict, total=False):
    tags: Optional[GitTagFilterCriteria]
    branches: Optional[GitBranchFilterCriteria]
    filePaths: Optional[GitFilePathFilterCriteria]


GitPushFilterList = List[GitPushFilter]


class GitConfiguration(TypedDict, total=False):
    sourceActionName: ActionName
    push: Optional[GitPushFilterList]
    pullRequest: Optional[GitPullRequestFilterList]


class PipelineTriggerDeclaration(TypedDict, total=False):
    providerType: PipelineTriggerProviderType
    gitConfiguration: GitConfiguration


PipelineTriggerDeclarationList = List[PipelineTriggerDeclaration]


class PipelineVariableDeclaration(TypedDict, total=False):
    name: PipelineVariableName
    defaultValue: Optional[PipelineVariableValue]
    description: Optional[PipelineVariableDescription]


PipelineVariableDeclarationList = List[PipelineVariableDeclaration]


class SuccessConditions(TypedDict, total=False):
    conditions: ConditionList


class RetryConfiguration(TypedDict, total=False):
    retryMode: Optional[StageRetryMode]


class FailureConditions(TypedDict, total=False):
    result: Optional[Result]
    retryConfiguration: Optional[RetryConfiguration]
    conditions: Optional[ConditionList]


StageActionDeclarationList = List[ActionDeclaration]
StageBlockerDeclarationList = List[BlockerDeclaration]


class StageDeclaration(TypedDict, total=False):
    name: StageName
    blockers: Optional[StageBlockerDeclarationList]
    actions: StageActionDeclarationList
    onFailure: Optional[FailureConditions]
    onSuccess: Optional[SuccessConditions]
    beforeEntry: Optional[BeforeEntryConditions]


PipelineStageDeclarationList = List[StageDeclaration]


class PipelineDeclaration(TypedDict, total=False):
    name: PipelineName
    roleArn: RoleArn
    artifactStore: Optional[ArtifactStore]
    artifactStores: Optional[ArtifactStoreMap]
    stages: PipelineStageDeclarationList
    version: Optional[PipelineVersion]
    executionMode: Optional[ExecutionMode]
    pipelineType: Optional[PipelineType]
    variables: Optional[PipelineVariableDeclarationList]
    triggers: Optional[PipelineTriggerDeclarationList]


class CreatePipelineInput(ServiceRequest):
    pipeline: PipelineDeclaration
    tags: Optional[TagList]


class CreatePipelineOutput(TypedDict, total=False):
    pipeline: Optional[PipelineDeclaration]
    tags: Optional[TagList]


Time = datetime


class CurrentRevision(TypedDict, total=False):
    revision: Revision
    changeIdentifier: RevisionChangeIdentifier
    created: Optional[Time]
    revisionSummary: Optional[RevisionSummary]


class DeleteCustomActionTypeInput(ServiceRequest):
    category: ActionCategory
    provider: ActionProvider
    version: Version


class DeletePipelineInput(ServiceRequest):
    name: PipelineName


class DeleteWebhookInput(ServiceRequest):
    name: WebhookName


class DeleteWebhookOutput(TypedDict, total=False):
    pass


class DeregisterWebhookWithThirdPartyInput(ServiceRequest):
    webhookName: Optional[WebhookName]


class DeregisterWebhookWithThirdPartyOutput(TypedDict, total=False):
    pass


class DisableStageTransitionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    transitionType: StageTransitionType
    reason: DisabledReason


class EnableStageTransitionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    transitionType: StageTransitionType


class ExecutionDetails(TypedDict, total=False):
    summary: Optional[ExecutionSummary]
    externalExecutionId: Optional[ExecutionId]
    percentComplete: Optional[Percentage]


class ExecutionTrigger(TypedDict, total=False):
    triggerType: Optional[TriggerType]
    triggerDetail: Optional[TriggerDetail]


FailureDetails = TypedDict(
    "FailureDetails",
    {
        "type": FailureType,
        "message": Message,
        "externalExecutionId": Optional[ExecutionId],
    },
    total=False,
)


class GetActionTypeInput(ServiceRequest):
    category: ActionCategory
    owner: ActionTypeOwner
    provider: ActionProvider
    version: Version


class GetActionTypeOutput(TypedDict, total=False):
    actionType: Optional[ActionTypeDeclaration]


class GetJobDetailsInput(ServiceRequest):
    jobId: JobId


class StageContext(TypedDict, total=False):
    name: Optional[StageName]


class PipelineContext(TypedDict, total=False):
    pipelineName: Optional[PipelineName]
    stage: Optional[StageContext]
    action: Optional[ActionContext]
    pipelineArn: Optional[PipelineArn]
    pipelineExecutionId: Optional[PipelineExecutionId]


class JobData(TypedDict, total=False):
    actionTypeId: Optional[ActionTypeId]
    actionConfiguration: Optional[ActionConfiguration]
    pipelineContext: Optional[PipelineContext]
    inputArtifacts: Optional[ArtifactList]
    outputArtifacts: Optional[ArtifactList]
    artifactCredentials: Optional[AWSSessionCredentials]
    continuationToken: Optional[ContinuationToken]
    encryptionKey: Optional[EncryptionKey]


class JobDetails(TypedDict, total=False):
    id: Optional[JobId]
    data: Optional[JobData]
    accountId: Optional[AccountId]


class GetJobDetailsOutput(TypedDict, total=False):
    jobDetails: Optional[JobDetails]


class GetPipelineExecutionInput(ServiceRequest):
    pipelineName: PipelineName
    pipelineExecutionId: PipelineExecutionId


class PipelineRollbackMetadata(TypedDict, total=False):
    rollbackTargetPipelineExecutionId: Optional[PipelineExecutionId]


class ResolvedPipelineVariable(TypedDict, total=False):
    name: Optional[String]
    resolvedValue: Optional[String]


ResolvedPipelineVariableList = List[ResolvedPipelineVariable]


class PipelineExecution(TypedDict, total=False):
    pipelineName: Optional[PipelineName]
    pipelineVersion: Optional[PipelineVersion]
    pipelineExecutionId: Optional[PipelineExecutionId]
    status: Optional[PipelineExecutionStatus]
    statusSummary: Optional[PipelineExecutionStatusSummary]
    artifactRevisions: Optional[ArtifactRevisionList]
    variables: Optional[ResolvedPipelineVariableList]
    trigger: Optional[ExecutionTrigger]
    executionMode: Optional[ExecutionMode]
    executionType: Optional[ExecutionType]
    rollbackMetadata: Optional[PipelineRollbackMetadata]


class GetPipelineExecutionOutput(TypedDict, total=False):
    pipelineExecution: Optional[PipelineExecution]


class GetPipelineInput(ServiceRequest):
    name: PipelineName
    version: Optional[PipelineVersion]


class PipelineMetadata(TypedDict, total=False):
    pipelineArn: Optional[PipelineArn]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]
    pollingDisabledAt: Optional[Timestamp]


class GetPipelineOutput(TypedDict, total=False):
    pipeline: Optional[PipelineDeclaration]
    metadata: Optional[PipelineMetadata]


class GetPipelineStateInput(ServiceRequest):
    name: PipelineName


class RetryStageMetadata(TypedDict, total=False):
    autoStageRetryAttempt: Optional[RetryAttempt]
    manualStageRetryAttempt: Optional[RetryAttempt]
    latestRetryTrigger: Optional[RetryTrigger]


class StageConditionsExecution(TypedDict, total=False):
    status: Optional[ConditionExecutionStatus]
    summary: Optional[ExecutionSummary]


class StageConditionState(TypedDict, total=False):
    latestExecution: Optional[StageConditionsExecution]
    conditionStates: Optional[ConditionStateList]


StageExecution = TypedDict(
    "StageExecution",
    {
        "pipelineExecutionId": PipelineExecutionId,
        "status": StageExecutionStatus,
        "type": Optional[ExecutionType],
    },
    total=False,
)
LastChangedAt = datetime


class TransitionState(TypedDict, total=False):
    enabled: Optional[Enabled]
    lastChangedBy: Optional[LastChangedBy]
    lastChangedAt: Optional[LastChangedAt]
    disabledReason: Optional[DisabledReason]


StageExecutionList = List[StageExecution]


class StageState(TypedDict, total=False):
    stageName: Optional[StageName]
    inboundExecution: Optional[StageExecution]
    inboundExecutions: Optional[StageExecutionList]
    inboundTransitionState: Optional[TransitionState]
    actionStates: Optional[ActionStateList]
    latestExecution: Optional[StageExecution]
    beforeEntryConditionState: Optional[StageConditionState]
    onSuccessConditionState: Optional[StageConditionState]
    onFailureConditionState: Optional[StageConditionState]
    retryStageMetadata: Optional[RetryStageMetadata]


StageStateList = List[StageState]


class GetPipelineStateOutput(TypedDict, total=False):
    pipelineName: Optional[PipelineName]
    pipelineVersion: Optional[PipelineVersion]
    stageStates: Optional[StageStateList]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]


class GetThirdPartyJobDetailsInput(ServiceRequest):
    jobId: ThirdPartyJobId
    clientToken: ClientToken


class ThirdPartyJobData(TypedDict, total=False):
    actionTypeId: Optional[ActionTypeId]
    actionConfiguration: Optional[ActionConfiguration]
    pipelineContext: Optional[PipelineContext]
    inputArtifacts: Optional[ArtifactList]
    outputArtifacts: Optional[ArtifactList]
    artifactCredentials: Optional[AWSSessionCredentials]
    continuationToken: Optional[ContinuationToken]
    encryptionKey: Optional[EncryptionKey]


class ThirdPartyJobDetails(TypedDict, total=False):
    id: Optional[ThirdPartyJobId]
    data: Optional[ThirdPartyJobData]
    nonce: Optional[Nonce]


class GetThirdPartyJobDetailsOutput(TypedDict, total=False):
    jobDetails: Optional[ThirdPartyJobDetails]


class Job(TypedDict, total=False):
    id: Optional[JobId]
    data: Optional[JobData]
    nonce: Optional[Nonce]
    accountId: Optional[AccountId]


JobList = List[Job]


class ListActionExecutionsInput(ServiceRequest):
    pipelineName: PipelineName
    filter: Optional[ActionExecutionFilter]
    maxResults: Optional[MaxResults]
    nextToken: Optional[NextToken]


class ListActionExecutionsOutput(TypedDict, total=False):
    actionExecutionDetails: Optional[ActionExecutionDetailList]
    nextToken: Optional[NextToken]


class ListActionTypesInput(ServiceRequest):
    actionOwnerFilter: Optional[ActionOwner]
    nextToken: Optional[NextToken]
    regionFilter: Optional[AWSRegionName]


class ListActionTypesOutput(TypedDict, total=False):
    actionTypes: ActionTypeList
    nextToken: Optional[NextToken]


class SucceededInStageFilter(TypedDict, total=False):
    stageName: Optional[StageName]


class PipelineExecutionFilter(TypedDict, total=False):
    succeededInStage: Optional[SucceededInStageFilter]


class ListPipelineExecutionsInput(ServiceRequest):
    pipelineName: PipelineName
    maxResults: Optional[MaxResults]
    filter: Optional[PipelineExecutionFilter]
    nextToken: Optional[NextToken]


class StopExecutionTrigger(TypedDict, total=False):
    reason: Optional[StopPipelineExecutionReason]


class SourceRevision(TypedDict, total=False):
    actionName: ActionName
    revisionId: Optional[Revision]
    revisionSummary: Optional[RevisionSummary]
    revisionUrl: Optional[Url]


SourceRevisionList = List[SourceRevision]


class PipelineExecutionSummary(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]
    status: Optional[PipelineExecutionStatus]
    statusSummary: Optional[PipelineExecutionStatusSummary]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    sourceRevisions: Optional[SourceRevisionList]
    trigger: Optional[ExecutionTrigger]
    stopTrigger: Optional[StopExecutionTrigger]
    executionMode: Optional[ExecutionMode]
    executionType: Optional[ExecutionType]
    rollbackMetadata: Optional[PipelineRollbackMetadata]


PipelineExecutionSummaryList = List[PipelineExecutionSummary]


class ListPipelineExecutionsOutput(TypedDict, total=False):
    pipelineExecutionSummaries: Optional[PipelineExecutionSummaryList]
    nextToken: Optional[NextToken]


class ListPipelinesInput(ServiceRequest):
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxPipelines]


class PipelineSummary(TypedDict, total=False):
    name: Optional[PipelineName]
    version: Optional[PipelineVersion]
    pipelineType: Optional[PipelineType]
    executionMode: Optional[ExecutionMode]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]


PipelineList = List[PipelineSummary]


class ListPipelinesOutput(TypedDict, total=False):
    pipelines: Optional[PipelineList]
    nextToken: Optional[NextToken]


class RuleExecutionFilter(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter]


class ListRuleExecutionsInput(ServiceRequest):
    pipelineName: PipelineName
    filter: Optional[RuleExecutionFilter]
    maxResults: Optional[MaxResults]
    nextToken: Optional[NextToken]


class RuleExecutionResult(TypedDict, total=False):
    externalExecutionId: Optional[ExternalExecutionId]
    externalExecutionSummary: Optional[ExternalExecutionSummary]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]


class RuleExecutionOutput(TypedDict, total=False):
    executionResult: Optional[RuleExecutionResult]


ResolvedRuleConfigurationMap = Dict[String, String]


class RuleExecutionInput(TypedDict, total=False):
    ruleTypeId: Optional[RuleTypeId]
    configuration: Optional[RuleConfigurationMap]
    resolvedConfiguration: Optional[ResolvedRuleConfigurationMap]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    inputArtifacts: Optional[ArtifactDetailList]


class RuleExecutionDetail(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]
    ruleExecutionId: Optional[RuleExecutionId]
    pipelineVersion: Optional[PipelineVersion]
    stageName: Optional[StageName]
    ruleName: Optional[RuleName]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    updatedBy: Optional[LastUpdatedBy]
    status: Optional[RuleExecutionStatus]
    input: Optional[RuleExecutionInput]
    output: Optional[RuleExecutionOutput]


RuleExecutionDetailList = List[RuleExecutionDetail]


class ListRuleExecutionsOutput(TypedDict, total=False):
    ruleExecutionDetails: Optional[RuleExecutionDetailList]
    nextToken: Optional[NextToken]


class ListRuleTypesInput(ServiceRequest):
    ruleOwnerFilter: Optional[RuleOwner]
    regionFilter: Optional[AWSRegionName]


RuleConfigurationProperty = TypedDict(
    "RuleConfigurationProperty",
    {
        "name": RuleConfigurationKey,
        "required": Boolean,
        "key": Boolean,
        "secret": Boolean,
        "queryable": Optional[Boolean],
        "description": Optional[Description],
        "type": Optional[RuleConfigurationPropertyType],
    },
    total=False,
)
RuleConfigurationPropertyList = List[RuleConfigurationProperty]


class RuleTypeSettings(TypedDict, total=False):
    thirdPartyConfigurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class RuleType(TypedDict, total=False):
    id: RuleTypeId
    settings: Optional[RuleTypeSettings]
    ruleConfigurationProperties: Optional[RuleConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails


RuleTypeList = List[RuleType]


class ListRuleTypesOutput(TypedDict, total=False):
    ruleTypes: RuleTypeList


class ListTagsForResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxResults]


class ListTagsForResourceOutput(TypedDict, total=False):
    tags: Optional[TagList]
    nextToken: Optional[NextToken]


WebhookLastTriggered = datetime


class WebhookAuthConfiguration(TypedDict, total=False):
    AllowedIPRange: Optional[WebhookAuthConfigurationAllowedIPRange]
    SecretToken: Optional[WebhookAuthConfigurationSecretToken]


class WebhookFilterRule(TypedDict, total=False):
    jsonPath: JsonPath
    matchEquals: Optional[MatchEquals]


WebhookFilters = List[WebhookFilterRule]


class WebhookDefinition(TypedDict, total=False):
    name: WebhookName
    targetPipeline: PipelineName
    targetAction: ActionName
    filters: WebhookFilters
    authentication: WebhookAuthenticationType
    authenticationConfiguration: WebhookAuthConfiguration


class ListWebhookItem(TypedDict, total=False):
    definition: WebhookDefinition
    url: WebhookUrl
    errorMessage: Optional[WebhookErrorMessage]
    errorCode: Optional[WebhookErrorCode]
    lastTriggered: Optional[WebhookLastTriggered]
    arn: Optional[WebhookArn]
    tags: Optional[TagList]


class ListWebhooksInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


WebhookList = List[ListWebhookItem]


class ListWebhooksOutput(TypedDict, total=False):
    webhooks: Optional[WebhookList]
    NextToken: Optional[NextToken]


class OverrideStageConditionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    pipelineExecutionId: PipelineExecutionId
    conditionType: ConditionType


class PipelineVariable(TypedDict, total=False):
    name: PipelineVariableName
    value: PipelineVariableValue


PipelineVariableList = List[PipelineVariable]
QueryParamMap = Dict[ActionConfigurationKey, ActionConfigurationQueryableValue]


class PollForJobsInput(ServiceRequest):
    actionTypeId: ActionTypeId
    maxBatchSize: Optional[MaxBatchSize]
    queryParam: Optional[QueryParamMap]


class PollForJobsOutput(TypedDict, total=False):
    jobs: Optional[JobList]


class PollForThirdPartyJobsInput(ServiceRequest):
    actionTypeId: ActionTypeId
    maxBatchSize: Optional[MaxBatchSize]


class ThirdPartyJob(TypedDict, total=False):
    clientId: Optional[ClientId]
    jobId: Optional[JobId]


ThirdPartyJobList = List[ThirdPartyJob]


class PollForThirdPartyJobsOutput(TypedDict, total=False):
    jobs: Optional[ThirdPartyJobList]


class PutActionRevisionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    actionName: ActionName
    actionRevision: ActionRevision


class PutActionRevisionOutput(TypedDict, total=False):
    newRevision: Optional[Boolean]
    pipelineExecutionId: Optional[PipelineExecutionId]


class PutApprovalResultInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    actionName: ActionName
    result: ApprovalResult
    token: ApprovalToken


class PutApprovalResultOutput(TypedDict, total=False):
    approvedAt: Optional[Timestamp]


class PutJobFailureResultInput(ServiceRequest):
    jobId: JobId
    failureDetails: FailureDetails


class PutJobSuccessResultInput(ServiceRequest):
    jobId: JobId
    currentRevision: Optional[CurrentRevision]
    continuationToken: Optional[ContinuationToken]
    executionDetails: Optional[ExecutionDetails]
    outputVariables: Optional[OutputVariablesMap]


class PutThirdPartyJobFailureResultInput(ServiceRequest):
    jobId: ThirdPartyJobId
    clientToken: ClientToken
    failureDetails: FailureDetails


class PutThirdPartyJobSuccessResultInput(ServiceRequest):
    jobId: ThirdPartyJobId
    clientToken: ClientToken
    currentRevision: Optional[CurrentRevision]
    continuationToken: Optional[ContinuationToken]
    executionDetails: Optional[ExecutionDetails]


class PutWebhookInput(ServiceRequest):
    webhook: WebhookDefinition
    tags: Optional[TagList]


class PutWebhookOutput(TypedDict, total=False):
    webhook: Optional[ListWebhookItem]


class RegisterWebhookWithThirdPartyInput(ServiceRequest):
    webhookName: Optional[WebhookName]


class RegisterWebhookWithThirdPartyOutput(TypedDict, total=False):
    pass


class RetryStageExecutionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    pipelineExecutionId: PipelineExecutionId
    retryMode: StageRetryMode


class RetryStageExecutionOutput(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]


class RollbackStageInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    targetPipelineExecutionId: PipelineExecutionId


class RollbackStageOutput(TypedDict, total=False):
    pipelineExecutionId: PipelineExecutionId


class SourceRevisionOverride(TypedDict, total=False):
    actionName: ActionName
    revisionType: SourceRevisionType
    revisionValue: Revision


SourceRevisionOverrideList = List[SourceRevisionOverride]


class StartPipelineExecutionInput(ServiceRequest):
    name: PipelineName
    variables: Optional[PipelineVariableList]
    clientRequestToken: Optional[ClientRequestToken]
    sourceRevisions: Optional[SourceRevisionOverrideList]


class StartPipelineExecutionOutput(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]


class StopPipelineExecutionInput(ServiceRequest):
    pipelineName: PipelineName
    pipelineExecutionId: PipelineExecutionId
    abandon: Optional[Boolean]
    reason: Optional[StopPipelineExecutionReason]


class StopPipelineExecutionOutput(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    tagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateActionTypeInput(ServiceRequest):
    actionType: ActionTypeDeclaration


class UpdatePipelineInput(ServiceRequest):
    pipeline: PipelineDeclaration


class UpdatePipelineOutput(TypedDict, total=False):
    pipeline: Optional[PipelineDeclaration]


class CodepipelineApi:
    service = "codepipeline"
    version = "2015-07-09"

    @handler("AcknowledgeJob")
    def acknowledge_job(
        self, context: RequestContext, job_id: JobId, nonce: Nonce, **kwargs
    ) -> AcknowledgeJobOutput:
        raise NotImplementedError

    @handler("AcknowledgeThirdPartyJob")
    def acknowledge_third_party_job(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        nonce: Nonce,
        client_token: ClientToken,
        **kwargs,
    ) -> AcknowledgeThirdPartyJobOutput:
        raise NotImplementedError

    @handler("CreateCustomActionType")
    def create_custom_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        provider: ActionProvider,
        version: Version,
        input_artifact_details: ArtifactDetails,
        output_artifact_details: ArtifactDetails,
        settings: ActionTypeSettings = None,
        configuration_properties: ActionConfigurationPropertyList = None,
        tags: TagList = None,
        **kwargs,
    ) -> CreateCustomActionTypeOutput:
        raise NotImplementedError

    @handler("CreatePipeline")
    def create_pipeline(
        self, context: RequestContext, pipeline: PipelineDeclaration, tags: TagList = None, **kwargs
    ) -> CreatePipelineOutput:
        raise NotImplementedError

    @handler("DeleteCustomActionType")
    def delete_custom_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        provider: ActionProvider,
        version: Version,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("DeletePipeline")
    def delete_pipeline(self, context: RequestContext, name: PipelineName, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteWebhook")
    def delete_webhook(
        self, context: RequestContext, name: WebhookName, **kwargs
    ) -> DeleteWebhookOutput:
        raise NotImplementedError

    @handler("DeregisterWebhookWithThirdParty")
    def deregister_webhook_with_third_party(
        self, context: RequestContext, webhook_name: WebhookName = None, **kwargs
    ) -> DeregisterWebhookWithThirdPartyOutput:
        raise NotImplementedError

    @handler("DisableStageTransition")
    def disable_stage_transition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        transition_type: StageTransitionType,
        reason: DisabledReason,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("EnableStageTransition")
    def enable_stage_transition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        transition_type: StageTransitionType,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("GetActionType")
    def get_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        owner: ActionTypeOwner,
        provider: ActionProvider,
        version: Version,
        **kwargs,
    ) -> GetActionTypeOutput:
        raise NotImplementedError

    @handler("GetJobDetails")
    def get_job_details(
        self, context: RequestContext, job_id: JobId, **kwargs
    ) -> GetJobDetailsOutput:
        raise NotImplementedError

    @handler("GetPipeline")
    def get_pipeline(
        self, context: RequestContext, name: PipelineName, version: PipelineVersion = None, **kwargs
    ) -> GetPipelineOutput:
        raise NotImplementedError

    @handler("GetPipelineExecution")
    def get_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        pipeline_execution_id: PipelineExecutionId,
        **kwargs,
    ) -> GetPipelineExecutionOutput:
        raise NotImplementedError

    @handler("GetPipelineState")
    def get_pipeline_state(
        self, context: RequestContext, name: PipelineName, **kwargs
    ) -> GetPipelineStateOutput:
        raise NotImplementedError

    @handler("GetThirdPartyJobDetails")
    def get_third_party_job_details(
        self, context: RequestContext, job_id: ThirdPartyJobId, client_token: ClientToken, **kwargs
    ) -> GetThirdPartyJobDetailsOutput:
        raise NotImplementedError

    @handler("ListActionExecutions")
    def list_action_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        filter: ActionExecutionFilter = None,
        max_results: MaxResults = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListActionExecutionsOutput:
        raise NotImplementedError

    @handler("ListActionTypes")
    def list_action_types(
        self,
        context: RequestContext,
        action_owner_filter: ActionOwner = None,
        next_token: NextToken = None,
        region_filter: AWSRegionName = None,
        **kwargs,
    ) -> ListActionTypesOutput:
        raise NotImplementedError

    @handler("ListPipelineExecutions")
    def list_pipeline_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        max_results: MaxResults = None,
        filter: PipelineExecutionFilter = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListPipelineExecutionsOutput:
        raise NotImplementedError

    @handler("ListPipelines")
    def list_pipelines(
        self,
        context: RequestContext,
        next_token: NextToken = None,
        max_results: MaxPipelines = None,
        **kwargs,
    ) -> ListPipelinesOutput:
        raise NotImplementedError

    @handler("ListRuleExecutions")
    def list_rule_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        filter: RuleExecutionFilter = None,
        max_results: MaxResults = None,
        next_token: NextToken = None,
        **kwargs,
    ) -> ListRuleExecutionsOutput:
        raise NotImplementedError

    @handler("ListRuleTypes")
    def list_rule_types(
        self,
        context: RequestContext,
        rule_owner_filter: RuleOwner = None,
        region_filter: AWSRegionName = None,
        **kwargs,
    ) -> ListRuleTypesOutput:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        **kwargs,
    ) -> ListTagsForResourceOutput:
        raise NotImplementedError

    @handler("ListWebhooks")
    def list_webhooks(
        self,
        context: RequestContext,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        **kwargs,
    ) -> ListWebhooksOutput:
        raise NotImplementedError

    @handler("OverrideStageCondition")
    def override_stage_condition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        pipeline_execution_id: PipelineExecutionId,
        condition_type: ConditionType,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("PollForJobs")
    def poll_for_jobs(
        self,
        context: RequestContext,
        action_type_id: ActionTypeId,
        max_batch_size: MaxBatchSize = None,
        query_param: QueryParamMap = None,
        **kwargs,
    ) -> PollForJobsOutput:
        raise NotImplementedError

    @handler("PollForThirdPartyJobs")
    def poll_for_third_party_jobs(
        self,
        context: RequestContext,
        action_type_id: ActionTypeId,
        max_batch_size: MaxBatchSize = None,
        **kwargs,
    ) -> PollForThirdPartyJobsOutput:
        raise NotImplementedError

    @handler("PutActionRevision")
    def put_action_revision(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        action_name: ActionName,
        action_revision: ActionRevision,
        **kwargs,
    ) -> PutActionRevisionOutput:
        raise NotImplementedError

    @handler("PutApprovalResult")
    def put_approval_result(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        action_name: ActionName,
        result: ApprovalResult,
        token: ApprovalToken,
        **kwargs,
    ) -> PutApprovalResultOutput:
        raise NotImplementedError

    @handler("PutJobFailureResult")
    def put_job_failure_result(
        self, context: RequestContext, job_id: JobId, failure_details: FailureDetails, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("PutJobSuccessResult")
    def put_job_success_result(
        self,
        context: RequestContext,
        job_id: JobId,
        current_revision: CurrentRevision = None,
        continuation_token: ContinuationToken = None,
        execution_details: ExecutionDetails = None,
        output_variables: OutputVariablesMap = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("PutThirdPartyJobFailureResult")
    def put_third_party_job_failure_result(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        client_token: ClientToken,
        failure_details: FailureDetails,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("PutThirdPartyJobSuccessResult")
    def put_third_party_job_success_result(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        client_token: ClientToken,
        current_revision: CurrentRevision = None,
        continuation_token: ContinuationToken = None,
        execution_details: ExecutionDetails = None,
        **kwargs,
    ) -> None:
        raise NotImplementedError

    @handler("PutWebhook")
    def put_webhook(
        self, context: RequestContext, webhook: WebhookDefinition, tags: TagList = None, **kwargs
    ) -> PutWebhookOutput:
        raise NotImplementedError

    @handler("RegisterWebhookWithThirdParty")
    def register_webhook_with_third_party(
        self, context: RequestContext, webhook_name: WebhookName = None, **kwargs
    ) -> RegisterWebhookWithThirdPartyOutput:
        raise NotImplementedError

    @handler("RetryStageExecution")
    def retry_stage_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        pipeline_execution_id: PipelineExecutionId,
        retry_mode: StageRetryMode,
        **kwargs,
    ) -> RetryStageExecutionOutput:
        raise NotImplementedError

    @handler("RollbackStage")
    def rollback_stage(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        target_pipeline_execution_id: PipelineExecutionId,
        **kwargs,
    ) -> RollbackStageOutput:
        raise NotImplementedError

    @handler("StartPipelineExecution")
    def start_pipeline_execution(
        self,
        context: RequestContext,
        name: PipelineName,
        variables: PipelineVariableList = None,
        client_request_token: ClientRequestToken = None,
        source_revisions: SourceRevisionOverrideList = None,
        **kwargs,
    ) -> StartPipelineExecutionOutput:
        raise NotImplementedError

    @handler("StopPipelineExecution")
    def stop_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        pipeline_execution_id: PipelineExecutionId,
        abandon: Boolean = None,
        reason: StopPipelineExecutionReason = None,
        **kwargs,
    ) -> StopPipelineExecutionOutput:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        raise NotImplementedError

    @handler("UpdateActionType")
    def update_action_type(
        self, context: RequestContext, action_type: ActionTypeDeclaration, **kwargs
    ) -> None:
        raise NotImplementedError

    @handler("UpdatePipeline")
    def update_pipeline(
        self, context: RequestContext, pipeline: PipelineDeclaration, **kwargs
    ) -> UpdatePipelineOutput:
        raise NotImplementedError
