from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
BuildTimeOut = int
FleetCapacity = int
FleetName = str
GitCloneDepth = int
KeyInput = str
NonEmptyString = str
NonNegativeInt = int
PageSize = int
Percentage = float
ProjectDescription = str
ProjectName = str
ReportGroupName = str
SensitiveNonEmptyString = str
SensitiveString = str
String = str
TimeOut = int
ValueInput = str
WrapperBoolean = bool
WrapperDouble = float
WrapperInt = int


class ArtifactNamespace(StrEnum):
    NONE = "NONE"
    BUILD_ID = "BUILD_ID"


class ArtifactPackaging(StrEnum):
    NONE = "NONE"
    ZIP = "ZIP"


class ArtifactsType(StrEnum):
    CODEPIPELINE = "CODEPIPELINE"
    S3 = "S3"
    NO_ARTIFACTS = "NO_ARTIFACTS"


class AuthType(StrEnum):
    OAUTH = "OAUTH"
    BASIC_AUTH = "BASIC_AUTH"
    PERSONAL_ACCESS_TOKEN = "PERSONAL_ACCESS_TOKEN"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class BatchReportModeType(StrEnum):
    REPORT_INDIVIDUAL_BUILDS = "REPORT_INDIVIDUAL_BUILDS"
    REPORT_AGGREGATED_BATCH = "REPORT_AGGREGATED_BATCH"


class BucketOwnerAccess(StrEnum):
    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    FULL = "FULL"


class BuildBatchPhaseType(StrEnum):
    SUBMITTED = "SUBMITTED"
    DOWNLOAD_BATCHSPEC = "DOWNLOAD_BATCHSPEC"
    IN_PROGRESS = "IN_PROGRESS"
    COMBINE_ARTIFACTS = "COMBINE_ARTIFACTS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class BuildPhaseType(StrEnum):
    SUBMITTED = "SUBMITTED"
    QUEUED = "QUEUED"
    PROVISIONING = "PROVISIONING"
    DOWNLOAD_SOURCE = "DOWNLOAD_SOURCE"
    INSTALL = "INSTALL"
    PRE_BUILD = "PRE_BUILD"
    BUILD = "BUILD"
    POST_BUILD = "POST_BUILD"
    UPLOAD_ARTIFACTS = "UPLOAD_ARTIFACTS"
    FINALIZING = "FINALIZING"
    COMPLETED = "COMPLETED"


class CacheMode(StrEnum):
    LOCAL_DOCKER_LAYER_CACHE = "LOCAL_DOCKER_LAYER_CACHE"
    LOCAL_SOURCE_CACHE = "LOCAL_SOURCE_CACHE"
    LOCAL_CUSTOM_CACHE = "LOCAL_CUSTOM_CACHE"


class CacheType(StrEnum):
    NO_CACHE = "NO_CACHE"
    S3 = "S3"
    LOCAL = "LOCAL"


class ComputeType(StrEnum):
    BUILD_GENERAL1_SMALL = "BUILD_GENERAL1_SMALL"
    BUILD_GENERAL1_MEDIUM = "BUILD_GENERAL1_MEDIUM"
    BUILD_GENERAL1_LARGE = "BUILD_GENERAL1_LARGE"
    BUILD_GENERAL1_XLARGE = "BUILD_GENERAL1_XLARGE"
    BUILD_GENERAL1_2XLARGE = "BUILD_GENERAL1_2XLARGE"
    BUILD_LAMBDA_1GB = "BUILD_LAMBDA_1GB"
    BUILD_LAMBDA_2GB = "BUILD_LAMBDA_2GB"
    BUILD_LAMBDA_4GB = "BUILD_LAMBDA_4GB"
    BUILD_LAMBDA_8GB = "BUILD_LAMBDA_8GB"
    BUILD_LAMBDA_10GB = "BUILD_LAMBDA_10GB"
    ATTRIBUTE_BASED_COMPUTE = "ATTRIBUTE_BASED_COMPUTE"


class CredentialProviderType(StrEnum):
    SECRETS_MANAGER = "SECRETS_MANAGER"


class EnvironmentType(StrEnum):
    WINDOWS_CONTAINER = "WINDOWS_CONTAINER"
    LINUX_CONTAINER = "LINUX_CONTAINER"
    LINUX_GPU_CONTAINER = "LINUX_GPU_CONTAINER"
    ARM_CONTAINER = "ARM_CONTAINER"
    WINDOWS_SERVER_2019_CONTAINER = "WINDOWS_SERVER_2019_CONTAINER"
    LINUX_LAMBDA_CONTAINER = "LINUX_LAMBDA_CONTAINER"
    ARM_LAMBDA_CONTAINER = "ARM_LAMBDA_CONTAINER"
    LINUX_EC2 = "LINUX_EC2"
    ARM_EC2 = "ARM_EC2"
    WINDOWS_EC2 = "WINDOWS_EC2"
    MAC_ARM = "MAC_ARM"


class EnvironmentVariableType(StrEnum):
    PLAINTEXT = "PLAINTEXT"
    PARAMETER_STORE = "PARAMETER_STORE"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class FileSystemType(StrEnum):
    EFS = "EFS"


class FleetContextCode(StrEnum):
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    ACTION_REQUIRED = "ACTION_REQUIRED"
    PENDING_DELETION = "PENDING_DELETION"
    INSUFFICIENT_CAPACITY = "INSUFFICIENT_CAPACITY"


class FleetOverflowBehavior(StrEnum):
    QUEUE = "QUEUE"
    ON_DEMAND = "ON_DEMAND"


class FleetProxyRuleBehavior(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    DENY_ALL = "DENY_ALL"


class FleetProxyRuleEffectType(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"


class FleetProxyRuleType(StrEnum):
    DOMAIN = "DOMAIN"
    IP = "IP"


class FleetScalingMetricType(StrEnum):
    FLEET_UTILIZATION_RATE = "FLEET_UTILIZATION_RATE"


class FleetScalingType(StrEnum):
    TARGET_TRACKING_SCALING = "TARGET_TRACKING_SCALING"


class FleetSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class FleetStatusCode(StrEnum):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ROTATING = "ROTATING"
    PENDING_DELETION = "PENDING_DELETION"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ACTIVE = "ACTIVE"


class ImagePullCredentialsType(StrEnum):
    CODEBUILD = "CODEBUILD"
    SERVICE_ROLE = "SERVICE_ROLE"


class LanguageType(StrEnum):
    JAVA = "JAVA"
    PYTHON = "PYTHON"
    NODE_JS = "NODE_JS"
    RUBY = "RUBY"
    GOLANG = "GOLANG"
    DOCKER = "DOCKER"
    ANDROID = "ANDROID"
    DOTNET = "DOTNET"
    BASE = "BASE"
    PHP = "PHP"


class LogsConfigStatusType(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MachineType(StrEnum):
    GENERAL = "GENERAL"
    NVME = "NVME"


class PlatformType(StrEnum):
    DEBIAN = "DEBIAN"
    AMAZON_LINUX = "AMAZON_LINUX"
    UBUNTU = "UBUNTU"
    WINDOWS_SERVER = "WINDOWS_SERVER"


class ProjectSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ProjectVisibilityType(StrEnum):
    PUBLIC_READ = "PUBLIC_READ"
    PRIVATE = "PRIVATE"


class ReportCodeCoverageSortByType(StrEnum):
    LINE_COVERAGE_PERCENTAGE = "LINE_COVERAGE_PERCENTAGE"
    FILE_PATH = "FILE_PATH"


class ReportExportConfigType(StrEnum):
    S3 = "S3"
    NO_EXPORT = "NO_EXPORT"


class ReportGroupSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ReportGroupStatusType(StrEnum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ReportGroupTrendFieldType(StrEnum):
    PASS_RATE = "PASS_RATE"
    DURATION = "DURATION"
    TOTAL = "TOTAL"
    LINE_COVERAGE = "LINE_COVERAGE"
    LINES_COVERED = "LINES_COVERED"
    LINES_MISSED = "LINES_MISSED"
    BRANCH_COVERAGE = "BRANCH_COVERAGE"
    BRANCHES_COVERED = "BRANCHES_COVERED"
    BRANCHES_MISSED = "BRANCHES_MISSED"


class ReportPackagingType(StrEnum):
    ZIP = "ZIP"
    NONE = "NONE"


class ReportStatusType(StrEnum):
    GENERATING = "GENERATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    INCOMPLETE = "INCOMPLETE"
    DELETING = "DELETING"


class ReportType(StrEnum):
    TEST = "TEST"
    CODE_COVERAGE = "CODE_COVERAGE"


class RetryBuildBatchType(StrEnum):
    RETRY_ALL_BUILDS = "RETRY_ALL_BUILDS"
    RETRY_FAILED_BUILDS = "RETRY_FAILED_BUILDS"


class ServerType(StrEnum):
    GITHUB = "GITHUB"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"


class SharedResourceSortByType(StrEnum):
    ARN = "ARN"
    MODIFIED_TIME = "MODIFIED_TIME"


class SortOrderType(StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SourceAuthType(StrEnum):
    OAUTH = "OAUTH"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class SourceType(StrEnum):
    CODECOMMIT = "CODECOMMIT"
    CODEPIPELINE = "CODEPIPELINE"
    GITHUB = "GITHUB"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"
    S3 = "S3"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    NO_SOURCE = "NO_SOURCE"


class StatusType(StrEnum):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    FAULT = "FAULT"
    TIMED_OUT = "TIMED_OUT"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


class WebhookBuildType(StrEnum):
    BUILD = "BUILD"
    BUILD_BATCH = "BUILD_BATCH"


class WebhookFilterType(StrEnum):
    EVENT = "EVENT"
    BASE_REF = "BASE_REF"
    HEAD_REF = "HEAD_REF"
    ACTOR_ACCOUNT_ID = "ACTOR_ACCOUNT_ID"
    FILE_PATH = "FILE_PATH"
    COMMIT_MESSAGE = "COMMIT_MESSAGE"
    WORKFLOW_NAME = "WORKFLOW_NAME"
    TAG_NAME = "TAG_NAME"
    RELEASE_NAME = "RELEASE_NAME"
    REPOSITORY_NAME = "REPOSITORY_NAME"


class WebhookScopeType(StrEnum):
    GITHUB_ORGANIZATION = "GITHUB_ORGANIZATION"
    GITHUB_GLOBAL = "GITHUB_GLOBAL"
    GITLAB_GROUP = "GITLAB_GROUP"


class AccountLimitExceededException(ServiceException):
    code: str = "AccountLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400


class OAuthProviderException(ServiceException):
    code: str = "OAuthProviderException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsException(ServiceException):
    code: str = "ResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class AutoRetryConfig(TypedDict, total=False):
    autoRetryLimit: Optional[WrapperInt]
    autoRetryNumber: Optional[WrapperInt]
    nextAutoRetry: Optional[String]
    previousAutoRetry: Optional[String]


BuildIds = List[NonEmptyString]


class BatchDeleteBuildsInput(ServiceRequest):
    ids: BuildIds


class BuildNotDeleted(TypedDict, total=False):
    id: Optional[NonEmptyString]
    statusCode: Optional[String]


BuildsNotDeleted = List[BuildNotDeleted]


class BatchDeleteBuildsOutput(TypedDict, total=False):
    buildsDeleted: Optional[BuildIds]
    buildsNotDeleted: Optional[BuildsNotDeleted]


BuildBatchIds = List[NonEmptyString]


class BatchGetBuildBatchesInput(ServiceRequest):
    ids: BuildBatchIds


ResolvedArtifact = TypedDict(
    "ResolvedArtifact",
    {
        "type": Optional[ArtifactsType],
        "location": Optional[String],
        "identifier": Optional[String],
    },
    total=False,
)
ResolvedSecondaryArtifacts = List[ResolvedArtifact]
Timestamp = datetime


class BuildSummary(TypedDict, total=False):
    arn: Optional[String]
    requestedOn: Optional[Timestamp]
    buildStatus: Optional[StatusType]
    primaryArtifact: Optional[ResolvedArtifact]
    secondaryArtifacts: Optional[ResolvedSecondaryArtifacts]


BuildSummaries = List[BuildSummary]
Identifiers = List[NonEmptyString]


class BuildGroup(TypedDict, total=False):
    identifier: Optional[String]
    dependsOn: Optional[Identifiers]
    ignoreFailure: Optional[Boolean]
    currentBuildSummary: Optional[BuildSummary]
    priorBuildSummaryList: Optional[BuildSummaries]


BuildGroups = List[BuildGroup]
ComputeTypesAllowed = List[NonEmptyString]


class BatchRestrictions(TypedDict, total=False):
    maximumBuildsAllowed: Optional[WrapperInt]
    computeTypesAllowed: Optional[ComputeTypesAllowed]


class ProjectBuildBatchConfig(TypedDict, total=False):
    serviceRole: Optional[NonEmptyString]
    combineArtifacts: Optional[WrapperBoolean]
    restrictions: Optional[BatchRestrictions]
    timeoutInMins: Optional[WrapperInt]
    batchReportMode: Optional[BatchReportModeType]


ProjectFileSystemLocation = TypedDict(
    "ProjectFileSystemLocation",
    {
        "type": Optional[FileSystemType],
        "location": Optional[String],
        "mountPoint": Optional[String],
        "identifier": Optional[String],
        "mountOptions": Optional[String],
    },
    total=False,
)
ProjectFileSystemLocations = List[ProjectFileSystemLocation]
WrapperLong = int
SecurityGroupIds = List[NonEmptyString]
Subnets = List[NonEmptyString]


class VpcConfig(TypedDict, total=False):
    vpcId: Optional[NonEmptyString]
    subnets: Optional[Subnets]
    securityGroupIds: Optional[SecurityGroupIds]


class S3LogsConfig(TypedDict, total=False):
    status: LogsConfigStatusType
    location: Optional[String]
    encryptionDisabled: Optional[WrapperBoolean]
    bucketOwnerAccess: Optional[BucketOwnerAccess]


class CloudWatchLogsConfig(TypedDict, total=False):
    status: LogsConfigStatusType
    groupName: Optional[String]
    streamName: Optional[String]


class LogsConfig(TypedDict, total=False):
    cloudWatchLogs: Optional[CloudWatchLogsConfig]
    s3Logs: Optional[S3LogsConfig]


class RegistryCredential(TypedDict, total=False):
    credential: NonEmptyString
    credentialProvider: CredentialProviderType


EnvironmentVariable = TypedDict(
    "EnvironmentVariable",
    {
        "name": NonEmptyString,
        "value": String,
        "type": Optional[EnvironmentVariableType],
    },
    total=False,
)
EnvironmentVariables = List[EnvironmentVariable]


class ProjectFleet(TypedDict, total=False):
    fleetArn: Optional[String]


class ComputeConfiguration(TypedDict, total=False):
    vCpu: Optional[WrapperLong]
    memory: Optional[WrapperLong]
    disk: Optional[WrapperLong]
    machineType: Optional[MachineType]


ProjectEnvironment = TypedDict(
    "ProjectEnvironment",
    {
        "type": EnvironmentType,
        "image": NonEmptyString,
        "computeType": ComputeType,
        "computeConfiguration": Optional[ComputeConfiguration],
        "fleet": Optional[ProjectFleet],
        "environmentVariables": Optional[EnvironmentVariables],
        "privilegedMode": Optional[WrapperBoolean],
        "certificate": Optional[String],
        "registryCredential": Optional[RegistryCredential],
        "imagePullCredentialsType": Optional[ImagePullCredentialsType],
    },
    total=False,
)
ProjectCacheModes = List[CacheMode]
ProjectCache = TypedDict(
    "ProjectCache",
    {
        "type": CacheType,
        "location": Optional[String],
        "modes": Optional[ProjectCacheModes],
    },
    total=False,
)


class BuildArtifacts(TypedDict, total=False):
    location: Optional[String]
    sha256sum: Optional[String]
    md5sum: Optional[String]
    overrideArtifactName: Optional[WrapperBoolean]
    encryptionDisabled: Optional[WrapperBoolean]
    artifactIdentifier: Optional[String]
    bucketOwnerAccess: Optional[BucketOwnerAccess]


BuildArtifactsList = List[BuildArtifacts]


class ProjectSourceVersion(TypedDict, total=False):
    sourceIdentifier: String
    sourceVersion: String


ProjectSecondarySourceVersions = List[ProjectSourceVersion]


class BuildStatusConfig(TypedDict, total=False):
    context: Optional[String]
    targetUrl: Optional[String]


SourceAuth = TypedDict(
    "SourceAuth",
    {
        "type": SourceAuthType,
        "resource": Optional[String],
    },
    total=False,
)


class GitSubmodulesConfig(TypedDict, total=False):
    fetchSubmodules: WrapperBoolean


ProjectSource = TypedDict(
    "ProjectSource",
    {
        "type": SourceType,
        "location": Optional[String],
        "gitCloneDepth": Optional[GitCloneDepth],
        "gitSubmodulesConfig": Optional[GitSubmodulesConfig],
        "buildspec": Optional[String],
        "auth": Optional[SourceAuth],
        "reportBuildStatus": Optional[WrapperBoolean],
        "buildStatusConfig": Optional[BuildStatusConfig],
        "insecureSsl": Optional[WrapperBoolean],
        "sourceIdentifier": Optional[String],
    },
    total=False,
)
ProjectSources = List[ProjectSource]


class PhaseContext(TypedDict, total=False):
    statusCode: Optional[String]
    message: Optional[String]


PhaseContexts = List[PhaseContext]


class BuildBatchPhase(TypedDict, total=False):
    phaseType: Optional[BuildBatchPhaseType]
    phaseStatus: Optional[StatusType]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    durationInSeconds: Optional[WrapperLong]
    contexts: Optional[PhaseContexts]


BuildBatchPhases = List[BuildBatchPhase]


class BuildBatch(TypedDict, total=False):
    id: Optional[NonEmptyString]
    arn: Optional[NonEmptyString]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    currentPhase: Optional[String]
    buildBatchStatus: Optional[StatusType]
    sourceVersion: Optional[NonEmptyString]
    resolvedSourceVersion: Optional[NonEmptyString]
    projectName: Optional[NonEmptyString]
    phases: Optional[BuildBatchPhases]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[BuildArtifacts]
    secondaryArtifacts: Optional[BuildArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    logConfig: Optional[LogsConfig]
    buildTimeoutInMinutes: Optional[WrapperInt]
    queuedTimeoutInMinutes: Optional[WrapperInt]
    complete: Optional[Boolean]
    initiator: Optional[String]
    vpcConfig: Optional[VpcConfig]
    encryptionKey: Optional[NonEmptyString]
    buildBatchNumber: Optional[WrapperLong]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    buildGroups: Optional[BuildGroups]
    debugSessionEnabled: Optional[WrapperBoolean]


BuildBatches = List[BuildBatch]


class BatchGetBuildBatchesOutput(TypedDict, total=False):
    buildBatches: Optional[BuildBatches]
    buildBatchesNotFound: Optional[BuildBatchIds]


class BatchGetBuildsInput(ServiceRequest):
    ids: BuildIds


class DebugSession(TypedDict, total=False):
    sessionEnabled: Optional[WrapperBoolean]
    sessionTarget: Optional[NonEmptyString]


BuildReportArns = List[String]


class ExportedEnvironmentVariable(TypedDict, total=False):
    name: Optional[NonEmptyString]
    value: Optional[String]


ExportedEnvironmentVariables = List[ExportedEnvironmentVariable]


class NetworkInterface(TypedDict, total=False):
    subnetId: Optional[NonEmptyString]
    networkInterfaceId: Optional[NonEmptyString]


class LogsLocation(TypedDict, total=False):
    groupName: Optional[String]
    streamName: Optional[String]
    deepLink: Optional[String]
    s3DeepLink: Optional[String]
    cloudWatchLogsArn: Optional[String]
    s3LogsArn: Optional[String]
    cloudWatchLogs: Optional[CloudWatchLogsConfig]
    s3Logs: Optional[S3LogsConfig]


class BuildPhase(TypedDict, total=False):
    phaseType: Optional[BuildPhaseType]
    phaseStatus: Optional[StatusType]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    durationInSeconds: Optional[WrapperLong]
    contexts: Optional[PhaseContexts]


BuildPhases = List[BuildPhase]


class Build(TypedDict, total=False):
    id: Optional[NonEmptyString]
    arn: Optional[NonEmptyString]
    buildNumber: Optional[WrapperLong]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    currentPhase: Optional[String]
    buildStatus: Optional[StatusType]
    sourceVersion: Optional[NonEmptyString]
    resolvedSourceVersion: Optional[NonEmptyString]
    projectName: Optional[NonEmptyString]
    phases: Optional[BuildPhases]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[BuildArtifacts]
    secondaryArtifacts: Optional[BuildArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    logs: Optional[LogsLocation]
    timeoutInMinutes: Optional[WrapperInt]
    queuedTimeoutInMinutes: Optional[WrapperInt]
    buildComplete: Optional[Boolean]
    initiator: Optional[String]
    vpcConfig: Optional[VpcConfig]
    networkInterface: Optional[NetworkInterface]
    encryptionKey: Optional[NonEmptyString]
    exportedEnvironmentVariables: Optional[ExportedEnvironmentVariables]
    reportArns: Optional[BuildReportArns]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    debugSession: Optional[DebugSession]
    buildBatchArn: Optional[String]
    autoRetryConfig: Optional[AutoRetryConfig]


Builds = List[Build]


class BatchGetBuildsOutput(TypedDict, total=False):
    builds: Optional[Builds]
    buildsNotFound: Optional[BuildIds]


FleetNames = List[NonEmptyString]


class BatchGetFleetsInput(ServiceRequest):
    names: FleetNames


class Tag(TypedDict, total=False):
    key: Optional[KeyInput]
    value: Optional[ValueInput]


TagList = List[Tag]
FleetProxyRuleEntities = List[String]
FleetProxyRule = TypedDict(
    "FleetProxyRule",
    {
        "type": FleetProxyRuleType,
        "effect": FleetProxyRuleEffectType,
        "entities": FleetProxyRuleEntities,
    },
    total=False,
)
FleetProxyRules = List[FleetProxyRule]


class ProxyConfiguration(TypedDict, total=False):
    defaultBehavior: Optional[FleetProxyRuleBehavior]
    orderedProxyRules: Optional[FleetProxyRules]


class TargetTrackingScalingConfiguration(TypedDict, total=False):
    metricType: Optional[FleetScalingMetricType]
    targetValue: Optional[WrapperDouble]


TargetTrackingScalingConfigurations = List[TargetTrackingScalingConfiguration]


class ScalingConfigurationOutput(TypedDict, total=False):
    scalingType: Optional[FleetScalingType]
    targetTrackingScalingConfigs: Optional[TargetTrackingScalingConfigurations]
    maxCapacity: Optional[FleetCapacity]
    desiredCapacity: Optional[FleetCapacity]


class FleetStatus(TypedDict, total=False):
    statusCode: Optional[FleetStatusCode]
    context: Optional[FleetContextCode]
    message: Optional[String]


class Fleet(TypedDict, total=False):
    arn: Optional[NonEmptyString]
    name: Optional[FleetName]
    id: Optional[NonEmptyString]
    created: Optional[Timestamp]
    lastModified: Optional[Timestamp]
    status: Optional[FleetStatus]
    baseCapacity: Optional[FleetCapacity]
    environmentType: Optional[EnvironmentType]
    computeType: Optional[ComputeType]
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationOutput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


Fleets = List[Fleet]


class BatchGetFleetsOutput(TypedDict, total=False):
    fleets: Optional[Fleets]
    fleetsNotFound: Optional[FleetNames]


ProjectNames = List[NonEmptyString]


class BatchGetProjectsInput(ServiceRequest):
    names: ProjectNames


class ProjectBadge(TypedDict, total=False):
    badgeEnabled: Optional[Boolean]
    badgeRequestUrl: Optional[String]


class ScopeConfiguration(TypedDict, total=False):
    name: String
    domain: Optional[String]
    scope: WebhookScopeType


WebhookFilter = TypedDict(
    "WebhookFilter",
    {
        "type": WebhookFilterType,
        "pattern": String,
        "excludeMatchedPattern": Optional[WrapperBoolean],
    },
    total=False,
)
FilterGroup = List[WebhookFilter]
FilterGroups = List[FilterGroup]


class Webhook(TypedDict, total=False):
    url: Optional[NonEmptyString]
    payloadUrl: Optional[NonEmptyString]
    secret: Optional[NonEmptyString]
    branchFilter: Optional[String]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]
    manualCreation: Optional[WrapperBoolean]
    lastModifiedSecret: Optional[Timestamp]
    scopeConfiguration: Optional[ScopeConfiguration]


ProjectArtifacts = TypedDict(
    "ProjectArtifacts",
    {
        "type": ArtifactsType,
        "location": Optional[String],
        "path": Optional[String],
        "namespaceType": Optional[ArtifactNamespace],
        "name": Optional[String],
        "packaging": Optional[ArtifactPackaging],
        "overrideArtifactName": Optional[WrapperBoolean],
        "encryptionDisabled": Optional[WrapperBoolean],
        "artifactIdentifier": Optional[String],
        "bucketOwnerAccess": Optional[BucketOwnerAccess],
    },
    total=False,
)
ProjectArtifactsList = List[ProjectArtifacts]


class Project(TypedDict, total=False):
    name: Optional[ProjectName]
    arn: Optional[String]
    description: Optional[ProjectDescription]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[ProjectArtifacts]
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    created: Optional[Timestamp]
    lastModified: Optional[Timestamp]
    webhook: Optional[Webhook]
    vpcConfig: Optional[VpcConfig]
    badge: Optional[ProjectBadge]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    projectVisibility: Optional[ProjectVisibilityType]
    publicProjectAlias: Optional[NonEmptyString]
    resourceAccessRole: Optional[NonEmptyString]
    autoRetryLimit: Optional[WrapperInt]


Projects = List[Project]


class BatchGetProjectsOutput(TypedDict, total=False):
    projects: Optional[Projects]
    projectsNotFound: Optional[ProjectNames]


ReportGroupArns = List[NonEmptyString]


class BatchGetReportGroupsInput(ServiceRequest):
    reportGroupArns: ReportGroupArns


class S3ReportExportConfig(TypedDict, total=False):
    bucket: Optional[NonEmptyString]
    bucketOwner: Optional[String]
    path: Optional[String]
    packaging: Optional[ReportPackagingType]
    encryptionKey: Optional[NonEmptyString]
    encryptionDisabled: Optional[WrapperBoolean]


class ReportExportConfig(TypedDict, total=False):
    exportConfigType: Optional[ReportExportConfigType]
    s3Destination: Optional[S3ReportExportConfig]


ReportGroup = TypedDict(
    "ReportGroup",
    {
        "arn": Optional[NonEmptyString],
        "name": Optional[ReportGroupName],
        "type": Optional[ReportType],
        "exportConfig": Optional[ReportExportConfig],
        "created": Optional[Timestamp],
        "lastModified": Optional[Timestamp],
        "tags": Optional[TagList],
        "status": Optional[ReportGroupStatusType],
    },
    total=False,
)
ReportGroups = List[ReportGroup]


class BatchGetReportGroupsOutput(TypedDict, total=False):
    reportGroups: Optional[ReportGroups]
    reportGroupsNotFound: Optional[ReportGroupArns]


ReportArns = List[NonEmptyString]


class BatchGetReportsInput(ServiceRequest):
    reportArns: ReportArns


class CodeCoverageReportSummary(TypedDict, total=False):
    lineCoveragePercentage: Optional[Percentage]
    linesCovered: Optional[NonNegativeInt]
    linesMissed: Optional[NonNegativeInt]
    branchCoveragePercentage: Optional[Percentage]
    branchesCovered: Optional[NonNegativeInt]
    branchesMissed: Optional[NonNegativeInt]


ReportStatusCounts = Dict[String, WrapperInt]


class TestReportSummary(TypedDict, total=False):
    total: WrapperInt
    statusCounts: ReportStatusCounts
    durationInNanoSeconds: WrapperLong


Report = TypedDict(
    "Report",
    {
        "arn": Optional[NonEmptyString],
        "type": Optional[ReportType],
        "name": Optional[String],
        "reportGroupArn": Optional[NonEmptyString],
        "executionId": Optional[String],
        "status": Optional[ReportStatusType],
        "created": Optional[Timestamp],
        "expired": Optional[Timestamp],
        "exportConfig": Optional[ReportExportConfig],
        "truncated": Optional[WrapperBoolean],
        "testSummary": Optional[TestReportSummary],
        "codeCoverageSummary": Optional[CodeCoverageReportSummary],
    },
    total=False,
)
Reports = List[Report]


class BatchGetReportsOutput(TypedDict, total=False):
    reports: Optional[Reports]
    reportsNotFound: Optional[ReportArns]


class BuildBatchFilter(TypedDict, total=False):
    status: Optional[StatusType]


class CodeCoverage(TypedDict, total=False):
    id: Optional[NonEmptyString]
    reportARN: Optional[NonEmptyString]
    filePath: Optional[NonEmptyString]
    lineCoveragePercentage: Optional[Percentage]
    linesCovered: Optional[NonNegativeInt]
    linesMissed: Optional[NonNegativeInt]
    branchCoveragePercentage: Optional[Percentage]
    branchesCovered: Optional[NonNegativeInt]
    branchesMissed: Optional[NonNegativeInt]
    expired: Optional[Timestamp]


CodeCoverages = List[CodeCoverage]


class ScalingConfigurationInput(TypedDict, total=False):
    scalingType: Optional[FleetScalingType]
    targetTrackingScalingConfigs: Optional[TargetTrackingScalingConfigurations]
    maxCapacity: Optional[FleetCapacity]


class CreateFleetInput(ServiceRequest):
    name: FleetName
    baseCapacity: FleetCapacity
    environmentType: EnvironmentType
    computeType: ComputeType
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationInput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


class CreateFleetOutput(TypedDict, total=False):
    fleet: Optional[Fleet]


class CreateProjectInput(ServiceRequest):
    name: ProjectName
    description: Optional[ProjectDescription]
    source: ProjectSource
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: ProjectArtifacts
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: ProjectEnvironment
    serviceRole: NonEmptyString
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    vpcConfig: Optional[VpcConfig]
    badgeEnabled: Optional[WrapperBoolean]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    autoRetryLimit: Optional[WrapperInt]


class CreateProjectOutput(TypedDict, total=False):
    project: Optional[Project]


CreateReportGroupInput = TypedDict(
    "CreateReportGroupInput",
    {
        "name": ReportGroupName,
        "type": ReportType,
        "exportConfig": ReportExportConfig,
        "tags": Optional[TagList],
    },
    total=False,
)


class CreateReportGroupOutput(TypedDict, total=False):
    reportGroup: Optional[ReportGroup]


class CreateWebhookInput(ServiceRequest):
    projectName: ProjectName
    branchFilter: Optional[String]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]
    manualCreation: Optional[WrapperBoolean]
    scopeConfiguration: Optional[ScopeConfiguration]


class CreateWebhookOutput(TypedDict, total=False):
    webhook: Optional[Webhook]


class DeleteBuildBatchInput(ServiceRequest):
    id: NonEmptyString


class DeleteBuildBatchOutput(TypedDict, total=False):
    statusCode: Optional[String]
    buildsDeleted: Optional[BuildIds]
    buildsNotDeleted: Optional[BuildsNotDeleted]


class DeleteFleetInput(ServiceRequest):
    arn: NonEmptyString


class DeleteFleetOutput(TypedDict, total=False):
    pass


class DeleteProjectInput(ServiceRequest):
    name: NonEmptyString


class DeleteProjectOutput(TypedDict, total=False):
    pass


class DeleteReportGroupInput(ServiceRequest):
    arn: NonEmptyString
    deleteReports: Optional[Boolean]


class DeleteReportGroupOutput(TypedDict, total=False):
    pass


class DeleteReportInput(ServiceRequest):
    arn: NonEmptyString


class DeleteReportOutput(TypedDict, total=False):
    pass


class DeleteResourcePolicyInput(ServiceRequest):
    resourceArn: NonEmptyString


class DeleteResourcePolicyOutput(TypedDict, total=False):
    pass


class DeleteSourceCredentialsInput(ServiceRequest):
    arn: NonEmptyString


class DeleteSourceCredentialsOutput(TypedDict, total=False):
    arn: Optional[NonEmptyString]


class DeleteWebhookInput(ServiceRequest):
    projectName: ProjectName


class DeleteWebhookOutput(TypedDict, total=False):
    pass


class DescribeCodeCoveragesInput(ServiceRequest):
    reportArn: NonEmptyString
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[ReportCodeCoverageSortByType]
    minLineCoveragePercentage: Optional[Percentage]
    maxLineCoveragePercentage: Optional[Percentage]


class DescribeCodeCoveragesOutput(TypedDict, total=False):
    nextToken: Optional[String]
    codeCoverages: Optional[CodeCoverages]


class TestCaseFilter(TypedDict, total=False):
    status: Optional[String]
    keyword: Optional[String]


class DescribeTestCasesInput(ServiceRequest):
    reportArn: String
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    filter: Optional[TestCaseFilter]


class TestCase(TypedDict, total=False):
    reportArn: Optional[NonEmptyString]
    testRawDataPath: Optional[String]
    prefix: Optional[String]
    name: Optional[String]
    status: Optional[String]
    durationInNanoSeconds: Optional[WrapperLong]
    message: Optional[String]
    expired: Optional[Timestamp]


TestCases = List[TestCase]


class DescribeTestCasesOutput(TypedDict, total=False):
    nextToken: Optional[String]
    testCases: Optional[TestCases]


ImageVersions = List[String]


class EnvironmentImage(TypedDict, total=False):
    name: Optional[String]
    description: Optional[String]
    versions: Optional[ImageVersions]


EnvironmentImages = List[EnvironmentImage]


class EnvironmentLanguage(TypedDict, total=False):
    language: Optional[LanguageType]
    images: Optional[EnvironmentImages]


EnvironmentLanguages = List[EnvironmentLanguage]


class EnvironmentPlatform(TypedDict, total=False):
    platform: Optional[PlatformType]
    languages: Optional[EnvironmentLanguages]


EnvironmentPlatforms = List[EnvironmentPlatform]
FleetArns = List[NonEmptyString]


class GetReportGroupTrendInput(ServiceRequest):
    reportGroupArn: NonEmptyString
    numOfReports: Optional[PageSize]
    trendField: ReportGroupTrendFieldType


class ReportWithRawData(TypedDict, total=False):
    reportArn: Optional[NonEmptyString]
    data: Optional[String]


ReportGroupTrendRawDataList = List[ReportWithRawData]


class ReportGroupTrendStats(TypedDict, total=False):
    average: Optional[String]
    max: Optional[String]
    min: Optional[String]


class GetReportGroupTrendOutput(TypedDict, total=False):
    stats: Optional[ReportGroupTrendStats]
    rawData: Optional[ReportGroupTrendRawDataList]


class GetResourcePolicyInput(ServiceRequest):
    resourceArn: NonEmptyString


class GetResourcePolicyOutput(TypedDict, total=False):
    policy: Optional[NonEmptyString]


class ImportSourceCredentialsInput(ServiceRequest):
    username: Optional[NonEmptyString]
    token: SensitiveNonEmptyString
    serverType: ServerType
    authType: AuthType
    shouldOverwrite: Optional[WrapperBoolean]


class ImportSourceCredentialsOutput(TypedDict, total=False):
    arn: Optional[NonEmptyString]


class InvalidateProjectCacheInput(ServiceRequest):
    projectName: NonEmptyString


class InvalidateProjectCacheOutput(TypedDict, total=False):
    pass


class ListBuildBatchesForProjectInput(ServiceRequest):
    projectName: Optional[NonEmptyString]
    filter: Optional[BuildBatchFilter]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildBatchesForProjectOutput(TypedDict, total=False):
    ids: Optional[BuildBatchIds]
    nextToken: Optional[String]


class ListBuildBatchesInput(ServiceRequest):
    filter: Optional[BuildBatchFilter]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildBatchesOutput(TypedDict, total=False):
    ids: Optional[BuildBatchIds]
    nextToken: Optional[String]


class ListBuildsForProjectInput(ServiceRequest):
    projectName: NonEmptyString
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildsForProjectOutput(TypedDict, total=False):
    ids: Optional[BuildIds]
    nextToken: Optional[String]


class ListBuildsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildsOutput(TypedDict, total=False):
    ids: Optional[BuildIds]
    nextToken: Optional[String]


class ListCuratedEnvironmentImagesInput(ServiceRequest):
    pass


class ListCuratedEnvironmentImagesOutput(TypedDict, total=False):
    platforms: Optional[EnvironmentPlatforms]


class ListFleetsInput(ServiceRequest):
    nextToken: Optional[SensitiveString]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[FleetSortByType]


class ListFleetsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    fleets: Optional[FleetArns]


class ListProjectsInput(ServiceRequest):
    sortBy: Optional[ProjectSortByType]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[NonEmptyString]


class ListProjectsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    projects: Optional[ProjectNames]


class ListReportGroupsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[ReportGroupSortByType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]


class ListReportGroupsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reportGroups: Optional[ReportGroupArns]


class ReportFilter(TypedDict, total=False):
    status: Optional[ReportStatusType]


class ListReportsForReportGroupInput(ServiceRequest):
    reportGroupArn: String
    nextToken: Optional[String]
    sortOrder: Optional[SortOrderType]
    maxResults: Optional[PageSize]
    filter: Optional[ReportFilter]


class ListReportsForReportGroupOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reports: Optional[ReportArns]


class ListReportsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    filter: Optional[ReportFilter]


class ListReportsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reports: Optional[ReportArns]


class ListSharedProjectsInput(ServiceRequest):
    sortBy: Optional[SharedResourceSortByType]
    sortOrder: Optional[SortOrderType]
    maxResults: Optional[PageSize]
    nextToken: Optional[NonEmptyString]


ProjectArns = List[NonEmptyString]


class ListSharedProjectsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    projects: Optional[ProjectArns]


class ListSharedReportGroupsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[SharedResourceSortByType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]


class ListSharedReportGroupsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reportGroups: Optional[ReportGroupArns]


class ListSourceCredentialsInput(ServiceRequest):
    pass


class SourceCredentialsInfo(TypedDict, total=False):
    arn: Optional[NonEmptyString]
    serverType: Optional[ServerType]
    authType: Optional[AuthType]
    resource: Optional[String]


SourceCredentialsInfos = List[SourceCredentialsInfo]


class ListSourceCredentialsOutput(TypedDict, total=False):
    sourceCredentialsInfos: Optional[SourceCredentialsInfos]


class PutResourcePolicyInput(ServiceRequest):
    policy: NonEmptyString
    resourceArn: NonEmptyString


class PutResourcePolicyOutput(TypedDict, total=False):
    resourceArn: Optional[NonEmptyString]


class RetryBuildBatchInput(ServiceRequest):
    id: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    retryType: Optional[RetryBuildBatchType]


class RetryBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class RetryBuildInput(ServiceRequest):
    id: Optional[NonEmptyString]
    idempotencyToken: Optional[String]


class RetryBuildOutput(TypedDict, total=False):
    build: Optional[Build]


class StartBuildBatchInput(ServiceRequest):
    projectName: NonEmptyString
    secondarySourcesOverride: Optional[ProjectSources]
    secondarySourcesVersionOverride: Optional[ProjectSecondarySourceVersions]
    sourceVersion: Optional[String]
    artifactsOverride: Optional[ProjectArtifacts]
    secondaryArtifactsOverride: Optional[ProjectArtifactsList]
    environmentVariablesOverride: Optional[EnvironmentVariables]
    sourceTypeOverride: Optional[SourceType]
    sourceLocationOverride: Optional[String]
    sourceAuthOverride: Optional[SourceAuth]
    gitCloneDepthOverride: Optional[GitCloneDepth]
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig]
    buildspecOverride: Optional[String]
    insecureSslOverride: Optional[WrapperBoolean]
    reportBuildBatchStatusOverride: Optional[WrapperBoolean]
    environmentTypeOverride: Optional[EnvironmentType]
    imageOverride: Optional[NonEmptyString]
    computeTypeOverride: Optional[ComputeType]
    certificateOverride: Optional[String]
    cacheOverride: Optional[ProjectCache]
    serviceRoleOverride: Optional[NonEmptyString]
    privilegedModeOverride: Optional[WrapperBoolean]
    buildTimeoutInMinutesOverride: Optional[BuildTimeOut]
    queuedTimeoutInMinutesOverride: Optional[TimeOut]
    encryptionKeyOverride: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    logsConfigOverride: Optional[LogsConfig]
    registryCredentialOverride: Optional[RegistryCredential]
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsType]
    buildBatchConfigOverride: Optional[ProjectBuildBatchConfig]
    debugSessionEnabled: Optional[WrapperBoolean]


class StartBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class StartBuildInput(ServiceRequest):
    projectName: NonEmptyString
    secondarySourcesOverride: Optional[ProjectSources]
    secondarySourcesVersionOverride: Optional[ProjectSecondarySourceVersions]
    sourceVersion: Optional[String]
    artifactsOverride: Optional[ProjectArtifacts]
    secondaryArtifactsOverride: Optional[ProjectArtifactsList]
    environmentVariablesOverride: Optional[EnvironmentVariables]
    sourceTypeOverride: Optional[SourceType]
    sourceLocationOverride: Optional[String]
    sourceAuthOverride: Optional[SourceAuth]
    gitCloneDepthOverride: Optional[GitCloneDepth]
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig]
    buildspecOverride: Optional[String]
    insecureSslOverride: Optional[WrapperBoolean]
    reportBuildStatusOverride: Optional[WrapperBoolean]
    buildStatusConfigOverride: Optional[BuildStatusConfig]
    environmentTypeOverride: Optional[EnvironmentType]
    imageOverride: Optional[NonEmptyString]
    computeTypeOverride: Optional[ComputeType]
    certificateOverride: Optional[String]
    cacheOverride: Optional[ProjectCache]
    serviceRoleOverride: Optional[NonEmptyString]
    privilegedModeOverride: Optional[WrapperBoolean]
    timeoutInMinutesOverride: Optional[BuildTimeOut]
    queuedTimeoutInMinutesOverride: Optional[TimeOut]
    encryptionKeyOverride: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    logsConfigOverride: Optional[LogsConfig]
    registryCredentialOverride: Optional[RegistryCredential]
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsType]
    debugSessionEnabled: Optional[WrapperBoolean]
    fleetOverride: Optional[ProjectFleet]
    autoRetryLimitOverride: Optional[WrapperInt]


class StartBuildOutput(TypedDict, total=False):
    build: Optional[Build]


class StopBuildBatchInput(ServiceRequest):
    id: NonEmptyString


class StopBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class StopBuildInput(ServiceRequest):
    id: NonEmptyString


class StopBuildOutput(TypedDict, total=False):
    build: Optional[Build]


class UpdateFleetInput(ServiceRequest):
    arn: NonEmptyString
    baseCapacity: Optional[FleetCapacity]
    environmentType: Optional[EnvironmentType]
    computeType: Optional[ComputeType]
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationInput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


class UpdateFleetOutput(TypedDict, total=False):
    fleet: Optional[Fleet]


class UpdateProjectInput(ServiceRequest):
    name: NonEmptyString
    description: Optional[ProjectDescription]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[ProjectArtifacts]
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    vpcConfig: Optional[VpcConfig]
    badgeEnabled: Optional[WrapperBoolean]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    autoRetryLimit: Optional[WrapperInt]


class UpdateProjectOutput(TypedDict, total=False):
    project: Optional[Project]


class UpdateProjectVisibilityInput(ServiceRequest):
    projectArn: NonEmptyString
    projectVisibility: ProjectVisibilityType
    resourceAccessRole: Optional[NonEmptyString]


class UpdateProjectVisibilityOutput(TypedDict, total=False):
    projectArn: Optional[NonEmptyString]
    publicProjectAlias: Optional[NonEmptyString]
    projectVisibility: Optional[ProjectVisibilityType]


class UpdateReportGroupInput(ServiceRequest):
    arn: NonEmptyString
    exportConfig: Optional[ReportExportConfig]
    tags: Optional[TagList]


class UpdateReportGroupOutput(TypedDict, total=False):
    reportGroup: Optional[ReportGroup]


class UpdateWebhookInput(ServiceRequest):
    projectName: ProjectName
    branchFilter: Optional[String]
    rotateSecret: Optional[Boolean]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]


class UpdateWebhookOutput(TypedDict, total=False):
    webhook: Optional[Webhook]


class CodebuildApi:
    service = "codebuild"
    version = "2016-10-06"

    @handler("BatchDeleteBuilds")
    def batch_delete_builds(
        self, context: RequestContext, ids: BuildIds, **kwargs
    ) -> BatchDeleteBuildsOutput:
        raise NotImplementedError

    @handler("BatchGetBuildBatches")
    def batch_get_build_batches(
        self, context: RequestContext, ids: BuildBatchIds, **kwargs
    ) -> BatchGetBuildBatchesOutput:
        raise NotImplementedError

    @handler("BatchGetBuilds")
    def batch_get_builds(
        self, context: RequestContext, ids: BuildIds, **kwargs
    ) -> BatchGetBuildsOutput:
        raise NotImplementedError

    @handler("BatchGetFleets")
    def batch_get_fleets(
        self, context: RequestContext, names: FleetNames, **kwargs
    ) -> BatchGetFleetsOutput:
        raise NotImplementedError

    @handler("BatchGetProjects")
    def batch_get_projects(
        self, context: RequestContext, names: ProjectNames, **kwargs
    ) -> BatchGetProjectsOutput:
        raise NotImplementedError

    @handler("BatchGetReportGroups")
    def batch_get_report_groups(
        self, context: RequestContext, report_group_arns: ReportGroupArns, **kwargs
    ) -> BatchGetReportGroupsOutput:
        raise NotImplementedError

    @handler("BatchGetReports")
    def batch_get_reports(
        self, context: RequestContext, report_arns: ReportArns, **kwargs
    ) -> BatchGetReportsOutput:
        raise NotImplementedError

    @handler("CreateFleet")
    def create_fleet(
        self,
        context: RequestContext,
        name: FleetName,
        base_capacity: FleetCapacity,
        environment_type: EnvironmentType,
        compute_type: ComputeType,
        compute_configuration: ComputeConfiguration = None,
        scaling_configuration: ScalingConfigurationInput = None,
        overflow_behavior: FleetOverflowBehavior = None,
        vpc_config: VpcConfig = None,
        proxy_configuration: ProxyConfiguration = None,
        image_id: NonEmptyString = None,
        fleet_service_role: NonEmptyString = None,
        tags: TagList = None,
        **kwargs,
    ) -> CreateFleetOutput:
        raise NotImplementedError

    @handler("CreateProject")
    def create_project(
        self,
        context: RequestContext,
        name: ProjectName,
        source: ProjectSource,
        artifacts: ProjectArtifacts,
        environment: ProjectEnvironment,
        service_role: NonEmptyString,
        description: ProjectDescription = None,
        secondary_sources: ProjectSources = None,
        source_version: String = None,
        secondary_source_versions: ProjectSecondarySourceVersions = None,
        secondary_artifacts: ProjectArtifactsList = None,
        cache: ProjectCache = None,
        timeout_in_minutes: BuildTimeOut = None,
        queued_timeout_in_minutes: TimeOut = None,
        encryption_key: NonEmptyString = None,
        tags: TagList = None,
        vpc_config: VpcConfig = None,
        badge_enabled: WrapperBoolean = None,
        logs_config: LogsConfig = None,
        file_system_locations: ProjectFileSystemLocations = None,
        build_batch_config: ProjectBuildBatchConfig = None,
        concurrent_build_limit: WrapperInt = None,
        auto_retry_limit: WrapperInt = None,
        **kwargs,
    ) -> CreateProjectOutput:
        raise NotImplementedError

    @handler("CreateReportGroup", expand=False)
    def create_report_group(
        self, context: RequestContext, request: CreateReportGroupInput, **kwargs
    ) -> CreateReportGroupOutput:
        raise NotImplementedError

    @handler("CreateWebhook")
    def create_webhook(
        self,
        context: RequestContext,
        project_name: ProjectName,
        branch_filter: String = None,
        filter_groups: FilterGroups = None,
        build_type: WebhookBuildType = None,
        manual_creation: WrapperBoolean = None,
        scope_configuration: ScopeConfiguration = None,
        **kwargs,
    ) -> CreateWebhookOutput:
        raise NotImplementedError

    @handler("DeleteBuildBatch")
    def delete_build_batch(
        self, context: RequestContext, id: NonEmptyString, **kwargs
    ) -> DeleteBuildBatchOutput:
        raise NotImplementedError

    @handler("DeleteFleet")
    def delete_fleet(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteFleetOutput:
        raise NotImplementedError

    @handler("DeleteProject")
    def delete_project(
        self, context: RequestContext, name: NonEmptyString, **kwargs
    ) -> DeleteProjectOutput:
        raise NotImplementedError

    @handler("DeleteReport")
    def delete_report(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteReportOutput:
        raise NotImplementedError

    @handler("DeleteReportGroup")
    def delete_report_group(
        self, context: RequestContext, arn: NonEmptyString, delete_reports: Boolean = None, **kwargs
    ) -> DeleteReportGroupOutput:
        raise NotImplementedError

    @handler("DeleteResourcePolicy")
    def delete_resource_policy(
        self, context: RequestContext, resource_arn: NonEmptyString, **kwargs
    ) -> DeleteResourcePolicyOutput:
        raise NotImplementedError

    @handler("DeleteSourceCredentials")
    def delete_source_credentials(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteSourceCredentialsOutput:
        raise NotImplementedError

    @handler("DeleteWebhook")
    def delete_webhook(
        self, context: RequestContext, project_name: ProjectName, **kwargs
    ) -> DeleteWebhookOutput:
        raise NotImplementedError

    @handler("DescribeCodeCoverages")
    def describe_code_coverages(
        self,
        context: RequestContext,
        report_arn: NonEmptyString,
        next_token: String = None,
        max_results: PageSize = None,
        sort_order: SortOrderType = None,
        sort_by: ReportCodeCoverageSortByType = None,
        min_line_coverage_percentage: Percentage = None,
        max_line_coverage_percentage: Percentage = None,
        **kwargs,
    ) -> DescribeCodeCoveragesOutput:
        raise NotImplementedError

    @handler("DescribeTestCases")
    def describe_test_cases(
        self,
        context: RequestContext,
        report_arn: String,
        next_token: String = None,
        max_results: PageSize = None,
        filter: TestCaseFilter = None,
        **kwargs,
    ) -> DescribeTestCasesOutput:
        raise NotImplementedError

    @handler("GetReportGroupTrend")
    def get_report_group_trend(
        self,
        context: RequestContext,
        report_group_arn: NonEmptyString,
        trend_field: ReportGroupTrendFieldType,
        num_of_reports: PageSize = None,
        **kwargs,
    ) -> GetReportGroupTrendOutput:
        raise NotImplementedError

    @handler("GetResourcePolicy")
    def get_resource_policy(
        self, context: RequestContext, resource_arn: NonEmptyString, **kwargs
    ) -> GetResourcePolicyOutput:
        raise NotImplementedError

    @handler("ImportSourceCredentials")
    def import_source_credentials(
        self,
        context: RequestContext,
        token: SensitiveNonEmptyString,
        server_type: ServerType,
        auth_type: AuthType,
        username: NonEmptyString = None,
        should_overwrite: WrapperBoolean = None,
        **kwargs,
    ) -> ImportSourceCredentialsOutput:
        raise NotImplementedError

    @handler("InvalidateProjectCache")
    def invalidate_project_cache(
        self, context: RequestContext, project_name: NonEmptyString, **kwargs
    ) -> InvalidateProjectCacheOutput:
        raise NotImplementedError

    @handler("ListBuildBatches")
    def list_build_batches(
        self,
        context: RequestContext,
        filter: BuildBatchFilter = None,
        max_results: PageSize = None,
        sort_order: SortOrderType = None,
        next_token: String = None,
        **kwargs,
    ) -> ListBuildBatchesOutput:
        raise NotImplementedError

    @handler("ListBuildBatchesForProject")
    def list_build_batches_for_project(
        self,
        context: RequestContext,
        project_name: NonEmptyString = None,
        filter: BuildBatchFilter = None,
        max_results: PageSize = None,
        sort_order: SortOrderType = None,
        next_token: String = None,
        **kwargs,
    ) -> ListBuildBatchesForProjectOutput:
        raise NotImplementedError

    @handler("ListBuilds")
    def list_builds(
        self,
        context: RequestContext,
        sort_order: SortOrderType = None,
        next_token: String = None,
        **kwargs,
    ) -> ListBuildsOutput:
        raise NotImplementedError

    @handler("ListBuildsForProject")
    def list_builds_for_project(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        sort_order: SortOrderType = None,
        next_token: String = None,
        **kwargs,
    ) -> ListBuildsForProjectOutput:
        raise NotImplementedError

    @handler("ListCuratedEnvironmentImages")
    def list_curated_environment_images(
        self, context: RequestContext, **kwargs
    ) -> ListCuratedEnvironmentImagesOutput:
        raise NotImplementedError

    @handler("ListFleets")
    def list_fleets(
        self,
        context: RequestContext,
        next_token: SensitiveString = None,
        max_results: PageSize = None,
        sort_order: SortOrderType = None,
        sort_by: FleetSortByType = None,
        **kwargs,
    ) -> ListFleetsOutput:
        raise NotImplementedError

    @handler("ListProjects")
    def list_projects(
        self,
        context: RequestContext,
        sort_by: ProjectSortByType = None,
        sort_order: SortOrderType = None,
        next_token: NonEmptyString = None,
        **kwargs,
    ) -> ListProjectsOutput:
        raise NotImplementedError

    @handler("ListReportGroups")
    def list_report_groups(
        self,
        context: RequestContext,
        sort_order: SortOrderType = None,
        sort_by: ReportGroupSortByType = None,
        next_token: String = None,
        max_results: PageSize = None,
        **kwargs,
    ) -> ListReportGroupsOutput:
        raise NotImplementedError

    @handler("ListReports")
    def list_reports(
        self,
        context: RequestContext,
        sort_order: SortOrderType = None,
        next_token: String = None,
        max_results: PageSize = None,
        filter: ReportFilter = None,
        **kwargs,
    ) -> ListReportsOutput:
        raise NotImplementedError

    @handler("ListReportsForReportGroup")
    def list_reports_for_report_group(
        self,
        context: RequestContext,
        report_group_arn: String,
        next_token: String = None,
        sort_order: SortOrderType = None,
        max_results: PageSize = None,
        filter: ReportFilter = None,
        **kwargs,
    ) -> ListReportsForReportGroupOutput:
        raise NotImplementedError

    @handler("ListSharedProjects")
    def list_shared_projects(
        self,
        context: RequestContext,
        sort_by: SharedResourceSortByType = None,
        sort_order: SortOrderType = None,
        max_results: PageSize = None,
        next_token: NonEmptyString = None,
        **kwargs,
    ) -> ListSharedProjectsOutput:
        raise NotImplementedError

    @handler("ListSharedReportGroups")
    def list_shared_report_groups(
        self,
        context: RequestContext,
        sort_order: SortOrderType = None,
        sort_by: SharedResourceSortByType = None,
        next_token: String = None,
        max_results: PageSize = None,
        **kwargs,
    ) -> ListSharedReportGroupsOutput:
        raise NotImplementedError

    @handler("ListSourceCredentials")
    def list_source_credentials(
        self, context: RequestContext, **kwargs
    ) -> ListSourceCredentialsOutput:
        raise NotImplementedError

    @handler("PutResourcePolicy")
    def put_resource_policy(
        self,
        context: RequestContext,
        policy: NonEmptyString,
        resource_arn: NonEmptyString,
        **kwargs,
    ) -> PutResourcePolicyOutput:
        raise NotImplementedError

    @handler("RetryBuild")
    def retry_build(
        self,
        context: RequestContext,
        id: NonEmptyString = None,
        idempotency_token: String = None,
        **kwargs,
    ) -> RetryBuildOutput:
        raise NotImplementedError

    @handler("RetryBuildBatch")
    def retry_build_batch(
        self,
        context: RequestContext,
        id: NonEmptyString = None,
        idempotency_token: String = None,
        retry_type: RetryBuildBatchType = None,
        **kwargs,
    ) -> RetryBuildBatchOutput:
        raise NotImplementedError

    @handler("StartBuild")
    def start_build(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        secondary_sources_override: ProjectSources = None,
        secondary_sources_version_override: ProjectSecondarySourceVersions = None,
        source_version: String = None,
        artifacts_override: ProjectArtifacts = None,
        secondary_artifacts_override: ProjectArtifactsList = None,
        environment_variables_override: EnvironmentVariables = None,
        source_type_override: SourceType = None,
        source_location_override: String = None,
        source_auth_override: SourceAuth = None,
        git_clone_depth_override: GitCloneDepth = None,
        git_submodules_config_override: GitSubmodulesConfig = None,
        buildspec_override: String = None,
        insecure_ssl_override: WrapperBoolean = None,
        report_build_status_override: WrapperBoolean = None,
        build_status_config_override: BuildStatusConfig = None,
        environment_type_override: EnvironmentType = None,
        image_override: NonEmptyString = None,
        compute_type_override: ComputeType = None,
        certificate_override: String = None,
        cache_override: ProjectCache = None,
        service_role_override: NonEmptyString = None,
        privileged_mode_override: WrapperBoolean = None,
        timeout_in_minutes_override: BuildTimeOut = None,
        queued_timeout_in_minutes_override: TimeOut = None,
        encryption_key_override: NonEmptyString = None,
        idempotency_token: String = None,
        logs_config_override: LogsConfig = None,
        registry_credential_override: RegistryCredential = None,
        image_pull_credentials_type_override: ImagePullCredentialsType = None,
        debug_session_enabled: WrapperBoolean = None,
        fleet_override: ProjectFleet = None,
        auto_retry_limit_override: WrapperInt = None,
        **kwargs,
    ) -> StartBuildOutput:
        raise NotImplementedError

    @handler("StartBuildBatch")
    def start_build_batch(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        secondary_sources_override: ProjectSources = None,
        secondary_sources_version_override: ProjectSecondarySourceVersions = None,
        source_version: String = None,
        artifacts_override: ProjectArtifacts = None,
        secondary_artifacts_override: ProjectArtifactsList = None,
        environment_variables_override: EnvironmentVariables = None,
        source_type_override: SourceType = None,
        source_location_override: String = None,
        source_auth_override: SourceAuth = None,
        git_clone_depth_override: GitCloneDepth = None,
        git_submodules_config_override: GitSubmodulesConfig = None,
        buildspec_override: String = None,
        insecure_ssl_override: WrapperBoolean = None,
        report_build_batch_status_override: WrapperBoolean = None,
        environment_type_override: EnvironmentType = None,
        image_override: NonEmptyString = None,
        compute_type_override: ComputeType = None,
        certificate_override: String = None,
        cache_override: ProjectCache = None,
        service_role_override: NonEmptyString = None,
        privileged_mode_override: WrapperBoolean = None,
        build_timeout_in_minutes_override: BuildTimeOut = None,
        queued_timeout_in_minutes_override: TimeOut = None,
        encryption_key_override: NonEmptyString = None,
        idempotency_token: String = None,
        logs_config_override: LogsConfig = None,
        registry_credential_override: RegistryCredential = None,
        image_pull_credentials_type_override: ImagePullCredentialsType = None,
        build_batch_config_override: ProjectBuildBatchConfig = None,
        debug_session_enabled: WrapperBoolean = None,
        **kwargs,
    ) -> StartBuildBatchOutput:
        raise NotImplementedError

    @handler("StopBuild")
    def stop_build(self, context: RequestContext, id: NonEmptyString, **kwargs) -> StopBuildOutput:
        raise NotImplementedError

    @handler("StopBuildBatch")
    def stop_build_batch(
        self, context: RequestContext, id: NonEmptyString, **kwargs
    ) -> StopBuildBatchOutput:
        raise NotImplementedError

    @handler("UpdateFleet")
    def update_fleet(
        self,
        context: RequestContext,
        arn: NonEmptyString,
        base_capacity: FleetCapacity = None,
        environment_type: EnvironmentType = None,
        compute_type: ComputeType = None,
        compute_configuration: ComputeConfiguration = None,
        scaling_configuration: ScalingConfigurationInput = None,
        overflow_behavior: FleetOverflowBehavior = None,
        vpc_config: VpcConfig = None,
        proxy_configuration: ProxyConfiguration = None,
        image_id: NonEmptyString = None,
        fleet_service_role: NonEmptyString = None,
        tags: TagList = None,
        **kwargs,
    ) -> UpdateFleetOutput:
        raise NotImplementedError

    @handler("UpdateProject")
    def update_project(
        self,
        context: RequestContext,
        name: NonEmptyString,
        description: ProjectDescription = None,
        source: ProjectSource = None,
        secondary_sources: ProjectSources = None,
        source_version: String = None,
        secondary_source_versions: ProjectSecondarySourceVersions = None,
        artifacts: ProjectArtifacts = None,
        secondary_artifacts: ProjectArtifactsList = None,
        cache: ProjectCache = None,
        environment: ProjectEnvironment = None,
        service_role: NonEmptyString = None,
        timeout_in_minutes: BuildTimeOut = None,
        queued_timeout_in_minutes: TimeOut = None,
        encryption_key: NonEmptyString = None,
        tags: TagList = None,
        vpc_config: VpcConfig = None,
        badge_enabled: WrapperBoolean = None,
        logs_config: LogsConfig = None,
        file_system_locations: ProjectFileSystemLocations = None,
        build_batch_config: ProjectBuildBatchConfig = None,
        concurrent_build_limit: WrapperInt = None,
        auto_retry_limit: WrapperInt = None,
        **kwargs,
    ) -> UpdateProjectOutput:
        raise NotImplementedError

    @handler("UpdateProjectVisibility")
    def update_project_visibility(
        self,
        context: RequestContext,
        project_arn: NonEmptyString,
        project_visibility: ProjectVisibilityType,
        resource_access_role: NonEmptyString = None,
        **kwargs,
    ) -> UpdateProjectVisibilityOutput:
        raise NotImplementedError

    @handler("UpdateReportGroup")
    def update_report_group(
        self,
        context: RequestContext,
        arn: NonEmptyString,
        export_config: ReportExportConfig = None,
        tags: TagList = None,
        **kwargs,
    ) -> UpdateReportGroupOutput:
        raise NotImplementedError

    @handler("UpdateWebhook")
    def update_webhook(
        self,
        context: RequestContext,
        project_name: ProjectName,
        branch_filter: String = None,
        rotate_secret: Boolean = None,
        filter_groups: FilterGroups = None,
        build_type: WebhookBuildType = None,
        **kwargs,
    ) -> UpdateWebhookOutput:
        raise NotImplementedError
