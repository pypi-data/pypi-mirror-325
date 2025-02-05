from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import aws_cdk.aws_sqs as _aws_cdk_aws_sqs_ceddda9d


@jsii.data_type(
    jsii_type="@cdklabs/cdk-proserve-lib.types.AwsCustomResourceLambdaConfiguration",
    jsii_struct_bases=[],
    name_mapping={"subnets": "subnets", "vpc": "vpc"},
)
class AwsCustomResourceLambdaConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param subnets: (experimental) Optional subnet selection for the Lambda functions.
        :param vpc: (experimental) VPC where the Lambda functions will be deployed.

        :stability: experimental
        '''
        if isinstance(subnets, dict):
            subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c5cee93e244643d0253938483ebf4729a03d1dbc4432b65477c09475f2f439)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if subnets is not None:
            self._values["subnets"] = subnets
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''(experimental) Optional subnet selection for the Lambda functions.

        :stability: experimental
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''(experimental) VPC where the Lambda functions will be deployed.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsCustomResourceLambdaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsManagedPolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-proserve-lib.types.AwsManagedPolicy",
):
    '''(experimental) AWS Managed Policy.

    :stability: experimental
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADMINISTRATOR_ACCESS")
    def ADMINISTRATOR_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ADMINISTRATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADMINISTRATOR_ACCESS_AMPLIFY")
    def ADMINISTRATOR_ACCESS_AMPLIFY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ADMINISTRATOR_ACCESS_AMPLIFY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADMINISTRATOR_ACCESS_AWS_ELASTIC_BEANSTALK")
    def ADMINISTRATOR_ACCESS_AWS_ELASTIC_BEANSTALK(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ADMINISTRATOR_ACCESS_AWS_ELASTIC_BEANSTALK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AI_OPS_ASSISTANT_POLICY")
    def AI_OPS_ASSISTANT_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AI_OPS_ASSISTANT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AI_OPS_CONSOLE_ADMIN_POLICY")
    def AI_OPS_CONSOLE_ADMIN_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AI_OPS_CONSOLE_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AI_OPS_OPERATOR_ACCESS")
    def AI_OPS_OPERATOR_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AI_OPS_OPERATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AI_OPS_READ_ONLY_ACCESS")
    def AI_OPS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AI_OPS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_DEVICE_SETUP")
    def ALEXA_FOR_BUSINESS_DEVICE_SETUP(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_DEVICE_SETUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_FULL_ACCESS")
    def ALEXA_FOR_BUSINESS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION")
    def ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_LIFESIZE_DELEGATED_ACCESS_POLICY")
    def ALEXA_FOR_BUSINESS_LIFESIZE_DELEGATED_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_LIFESIZE_DELEGATED_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY")
    def ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS")
    def ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY_ADMINISTRATOR")
    def AMAZON_API_GATEWAY_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_API_GATEWAY_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS")
    def AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_FLOW_FULL_ACCESS")
    def AMAZON_APP_FLOW_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_APP_FLOW_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_FLOW_READ_ONLY_ACCESS")
    def AMAZON_APP_FLOW_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_APP_FLOW_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_FULL_ACCESS")
    def AMAZON_APP_STREAM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_APP_STREAM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_READ_ONLY_ACCESS")
    def AMAZON_APP_STREAM_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_APP_STREAM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ATHENA_FULL_ACCESS")
    def AMAZON_ATHENA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ATHENA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AUGMENTED_AI_FULL_ACCESS")
    def AMAZON_AUGMENTED_AI_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AUGMENTED_AI_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS")
    def AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AUGMENTED_AI_INTEGRATED_API_ACCESS")
    def AMAZON_AUGMENTED_AI_INTEGRATED_API_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AUGMENTED_AI_INTEGRATED_API_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AURORA_DSQL_CONSOLE_FULL_ACCESS")
    def AMAZON_AURORA_DSQL_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AURORA_DSQL_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AURORA_DSQL_FULL_ACCESS")
    def AMAZON_AURORA_DSQL_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AURORA_DSQL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AURORA_DSQL_READ_ONLY_ACCESS")
    def AMAZON_AURORA_DSQL_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_AURORA_DSQL_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_BEDROCK_FULL_ACCESS")
    def AMAZON_BEDROCK_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_BEDROCK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_BEDROCK_READ_ONLY")
    def AMAZON_BEDROCK_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_BEDROCK_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_BEDROCK_STUDIO_PERMISSIONS_BOUNDARY")
    def AMAZON_BEDROCK_STUDIO_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_BEDROCK_STUDIO_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_BRAKET_FULL_ACCESS")
    def AMAZON_BRAKET_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_BRAKET_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_BRAKET_JOBS_EXECUTION_POLICY")
    def AMAZON_BRAKET_JOBS_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_BRAKET_JOBS_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_FULL_ACCESS")
    def AMAZON_CHIME_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CHIME_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_READ_ONLY")
    def AMAZON_CHIME_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CHIME_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_SDK")
    def AMAZON_CHIME_SDK(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CHIME_SDK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_USER_MANAGEMENT")
    def AMAZON_CHIME_USER_MANAGEMENT(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CHIME_USER_MANAGEMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_DIRECTORY_FULL_ACCESS")
    def AMAZON_CLOUD_DIRECTORY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_DIRECTORY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS")
    def AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_EVIDENTLY_FULL_ACCESS")
    def AMAZON_CLOUD_WATCH_EVIDENTLY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_WATCH_EVIDENTLY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_EVIDENTLY_READ_ONLY_ACCESS")
    def AMAZON_CLOUD_WATCH_EVIDENTLY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_WATCH_EVIDENTLY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_RUM_FULL_ACCESS")
    def AMAZON_CLOUD_WATCH_RUM_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_WATCH_RUM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_RUM_READ_ONLY_ACCESS")
    def AMAZON_CLOUD_WATCH_RUM_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CLOUD_WATCH_RUM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_CATALYST_FULL_ACCESS")
    def AMAZON_CODE_CATALYST_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_CATALYST_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_CATALYST_READ_ONLY_ACCESS")
    def AMAZON_CODE_CATALYST_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_CATALYST_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_PROFILER_AGENT_ACCESS")
    def AMAZON_CODE_GURU_PROFILER_AGENT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_PROFILER_AGENT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_PROFILER_FULL_ACCESS")
    def AMAZON_CODE_GURU_PROFILER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_PROFILER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS")
    def AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS")
    def AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS")
    def AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_SECURITY_FULL_ACCESS")
    def AMAZON_CODE_GURU_SECURITY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_SECURITY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_SECURITY_SCAN_ACCESS")
    def AMAZON_CODE_GURU_SECURITY_SCAN_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CODE_GURU_SECURITY_SCAN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES")
    def AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_POWER_USER")
    def AMAZON_COGNITO_POWER_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_COGNITO_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_READ_ONLY")
    def AMAZON_COGNITO_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_COGNITO_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_UN_AUTHED_IDENTITIES_SESSION_POLICY")
    def AMAZON_COGNITO_UN_AUTHED_IDENTITIES_SESSION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_COGNITO_UN_AUTHED_IDENTITIES_SESSION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_UNAUTHENTICATED_IDENTITIES")
    def AMAZON_COGNITO_UNAUTHENTICATED_IDENTITIES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_COGNITO_UNAUTHENTICATED_IDENTITIES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_FULL_ACCESS")
    def AMAZON_CONNECT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CONNECT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_READ_ONLY_ACCESS")
    def AMAZON_CONNECT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CONNECT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_VOICE_ID_FULL_ACCESS")
    def AMAZON_CONNECT_VOICE_ID_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_CONNECT_VOICE_ID_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY")
    def AMAZON_DATA_ZONE_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_FULL_ACCESS")
    def AMAZON_DATA_ZONE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_FULL_USER_ACCESS")
    def AMAZON_DATA_ZONE_FULL_USER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_FULL_USER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_REDSHIFT_GLUE_PROVISIONING_POLICY")
    def AMAZON_DATA_ZONE_REDSHIFT_GLUE_PROVISIONING_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_REDSHIFT_GLUE_PROVISIONING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_SAGE_MAKER_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY")
    def AMAZON_DATA_ZONE_SAGE_MAKER_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_SAGE_MAKER_ENVIRONMENT_ROLE_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_SAGE_MAKER_MANAGE_ACCESS_ROLE_POLICY")
    def AMAZON_DATA_ZONE_SAGE_MAKER_MANAGE_ACCESS_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_SAGE_MAKER_MANAGE_ACCESS_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_ZONE_SAGE_MAKER_PROVISIONING_ROLE_POLICY")
    def AMAZON_DATA_ZONE_SAGE_MAKER_PROVISIONING_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DATA_ZONE_SAGE_MAKER_PROVISIONING_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DETECTIVE_FULL_ACCESS")
    def AMAZON_DETECTIVE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DETECTIVE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DETECTIVE_INVESTIGATOR_ACCESS")
    def AMAZON_DETECTIVE_INVESTIGATOR_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DETECTIVE_INVESTIGATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DETECTIVE_MEMBER_ACCESS")
    def AMAZON_DETECTIVE_MEMBER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DETECTIVE_MEMBER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DETECTIVE_ORGANIZATIONS_ACCESS")
    def AMAZON_DETECTIVE_ORGANIZATIONS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DETECTIVE_ORGANIZATIONS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DEV_OPS_GURU_CONSOLE_FULL_ACCESS")
    def AMAZON_DEV_OPS_GURU_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DEV_OPS_GURU_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DEV_OPS_GURU_FULL_ACCESS")
    def AMAZON_DEV_OPS_GURU_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DEV_OPS_GURU_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DEV_OPS_GURU_ORGANIZATIONS_ACCESS")
    def AMAZON_DEV_OPS_GURU_ORGANIZATIONS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DEV_OPS_GURU_ORGANIZATIONS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DEV_OPS_GURU_READ_ONLY_ACCESS")
    def AMAZON_DEV_OPS_GURU_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DEV_OPS_GURU_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_CONSOLE_FULL_ACCESS")
    def AMAZON_DOC_DB_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DOC_DB_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_ELASTIC_FULL_ACCESS")
    def AMAZON_DOC_DB_ELASTIC_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DOC_DB_ELASTIC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_ELASTIC_READ_ONLY_ACCESS")
    def AMAZON_DOC_DB_ELASTIC_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DOC_DB_ELASTIC_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_FULL_ACCESS")
    def AMAZON_DOC_DB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DOC_DB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_READ_ONLY_ACCESS")
    def AMAZON_DOC_DB_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DOC_DB_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DRSVPC_MANAGEMENT")
    def AMAZON_DRSVPC_MANAGEMENT(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DRSVPC_MANAGEMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_FULL_ACCESS")
    def AMAZON_DYNAMO_DB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DYNAMO_DB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE")
    def AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_READ_ONLY_ACCESS")
    def AMAZON_DYNAMO_DB_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_DYNAMO_DB_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS")
    def AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER")
    def AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_PULL_ONLY")
    def AMAZON_EC2_CONTAINER_REGISTRY_PULL_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_PULL_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY")
    def AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_FULL_ACCESS")
    def AMAZON_EC2_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_READ_ONLY_ACCESS")
    def AMAZON_EC2_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_ROLE_POLICY_FOR_LAUNCH_WIZARD")
    def AMAZON_EC2_ROLE_POLICY_FOR_LAUNCH_WIZARD(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EC2_ROLE_POLICY_FOR_LAUNCH_WIZARD"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ECS_FULL_ACCESS")
    def AMAZON_ECS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ECS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ECS_INFRASTRUCTURE_ROLE_POLICY_FOR_VPC_LATTICE")
    def AMAZON_ECS_INFRASTRUCTURE_ROLE_POLICY_FOR_VPC_LATTICE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ECS_INFRASTRUCTURE_ROLE_POLICY_FOR_VPC_LATTICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_BLOCK_STORAGE_POLICY")
    def AMAZON_EKS_BLOCK_STORAGE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_BLOCK_STORAGE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_CLUSTER_POLICY")
    def AMAZON_EKS_CLUSTER_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_CLUSTER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_CNI_POLICY")
    def AMAZON_EKS_CNI_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_CNI_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_COMPUTE_POLICY")
    def AMAZON_EKS_COMPUTE_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_COMPUTE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY")
    def AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_LOAD_BALANCING_POLICY")
    def AMAZON_EKS_LOAD_BALANCING_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_LOAD_BALANCING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_LOCAL_OUTPOST_CLUSTER_POLICY")
    def AMAZON_EKS_LOCAL_OUTPOST_CLUSTER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_LOCAL_OUTPOST_CLUSTER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_NETWORKING_POLICY")
    def AMAZON_EKS_NETWORKING_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_NETWORKING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_SERVICE_POLICY")
    def AMAZON_EKS_SERVICE_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_SERVICE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_WORKER_NODE_MINIMAL_POLICY")
    def AMAZON_EKS_WORKER_NODE_MINIMAL_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_WORKER_NODE_MINIMAL_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_WORKER_NODE_POLICY")
    def AMAZON_EKS_WORKER_NODE_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKS_WORKER_NODE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKSVPC_RESOURCE_CONTROLLER")
    def AMAZON_EKSVPC_RESOURCE_CONTROLLER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EKSVPC_RESOURCE_CONTROLLER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTI_CACHE_FULL_ACCESS")
    def AMAZON_ELASTI_CACHE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTI_CACHE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS")
    def AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_FULL_ACCESS")
    def AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_POWER_USER")
    def AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_POWER_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_READ_ONLY")
    def AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_REGISTRY_PUBLIC_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_FULL_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_WRITE_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_WRITE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_CLIENT_READ_WRITE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEMS_UTILS")
    def AMAZON_ELASTIC_FILE_SYSTEMS_UTILS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEMS_UTILS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS")
    def AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_PLACEMENT_GROUP_POLICY")
    def AMAZON_ELASTIC_MAP_REDUCE_PLACEMENT_GROUP_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_PLACEMENT_GROUP_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS")
    def AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER")
    def AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EMR_FULL_ACCESS_POLICY_V2")
    def AMAZON_EMR_FULL_ACCESS_POLICY_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EMR_FULL_ACCESS_POLICY_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EMR_READ_ONLY_ACCESS_POLICY_V2")
    def AMAZON_EMR_READ_ONLY_ACCESS_POLICY_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EMR_READ_ONLY_ACCESS_POLICY_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_COGNITO_ACCESS")
    def AMAZON_ES_COGNITO_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ES_COGNITO_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_FULL_ACCESS")
    def AMAZON_ES_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_READ_ONLY_ACCESS")
    def AMAZON_ES_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_PIPES_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_PIPES_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_PIPES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_PIPES_OPERATOR_ACCESS")
    def AMAZON_EVENT_BRIDGE_PIPES_OPERATOR_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_PIPES_OPERATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_PIPES_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_PIPES_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_PIPES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEDULER_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEDULER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEDULER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEDULER_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEDULER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEDULER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_CONSOLE_FULL_ACCESS")
    def AMAZON_F_SX_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_F_SX_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS")
    def AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_FULL_ACCESS")
    def AMAZON_F_SX_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_F_SX_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_READ_ONLY_ACCESS")
    def AMAZON_F_SX_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_F_SX_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FORECAST_FULL_ACCESS")
    def AMAZON_FORECAST_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_FORECAST_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY")
    def AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOS_FULL_ACCESS")
    def AMAZON_FREE_RTOS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_FREE_RTOS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GLACIER_FULL_ACCESS")
    def AMAZON_GLACIER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_GLACIER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GLACIER_READ_ONLY_ACCESS")
    def AMAZON_GLACIER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_GLACIER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY_FULL_ACCESS")
    def AMAZON_GUARD_DUTY_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_GUARD_DUTY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY_READ_ONLY_ACCESS")
    def AMAZON_GUARD_DUTY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_GUARD_DUTY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HEALTH_LAKE_FULL_ACCESS")
    def AMAZON_HEALTH_LAKE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HEALTH_LAKE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HEALTH_LAKE_READ_ONLY_ACCESS")
    def AMAZON_HEALTH_LAKE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HEALTH_LAKE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_FULL_ACCESS")
    def AMAZON_HONEYCODE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_READ_ONLY_ACCESS")
    def AMAZON_HONEYCODE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_TEAM_ASSOCIATION_FULL_ACCESS")
    def AMAZON_HONEYCODE_TEAM_ASSOCIATION_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_TEAM_ASSOCIATION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_TEAM_ASSOCIATION_READ_ONLY_ACCESS")
    def AMAZON_HONEYCODE_TEAM_ASSOCIATION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_TEAM_ASSOCIATION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_WORKBOOK_FULL_ACCESS")
    def AMAZON_HONEYCODE_WORKBOOK_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_WORKBOOK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_HONEYCODE_WORKBOOK_READ_ONLY_ACCESS")
    def AMAZON_HONEYCODE_WORKBOOK_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_HONEYCODE_WORKBOOK_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR_FULL_ACCESS")
    def AMAZON_INSPECTOR_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_INSPECTOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR_READ_ONLY_ACCESS")
    def AMAZON_INSPECTOR_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_INSPECTOR_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR2_FULL_ACCESS")
    def AMAZON_INSPECTOR2_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_INSPECTOR2_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR2_MANAGED_CIS_POLICY")
    def AMAZON_INSPECTOR2_MANAGED_CIS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_INSPECTOR2_MANAGED_CIS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR2_READ_ONLY_ACCESS")
    def AMAZON_INSPECTOR2_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_INSPECTOR2_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KENDRA_FULL_ACCESS")
    def AMAZON_KENDRA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KENDRA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KENDRA_READ_ONLY_ACCESS")
    def AMAZON_KENDRA_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KENDRA_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KEYSPACES_FULL_ACCESS")
    def AMAZON_KEYSPACES_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KEYSPACES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KEYSPACES_READ_ONLY_ACCESS")
    def AMAZON_KEYSPACES_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KEYSPACES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KEYSPACES_READ_ONLY_ACCESS_V2")
    def AMAZON_KEYSPACES_READ_ONLY_ACCESS_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KEYSPACES_READ_ONLY_ACCESS_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS_FULL_ACCESS")
    def AMAZON_KINESIS_ANALYTICS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS_READ_ONLY")
    def AMAZON_KINESIS_ANALYTICS_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FIREHOSE_FULL_ACCESS")
    def AMAZON_KINESIS_FIREHOSE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_FIREHOSE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FULL_ACCESS")
    def AMAZON_KINESIS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS")
    def AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LAUNCH_WIZARD_FULL_ACCESS_V2")
    def AMAZON_LAUNCH_WIZARD_FULL_ACCESS_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LAUNCH_WIZARD_FULL_ACCESS_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_FULL_ACCESS")
    def AMAZON_LEX_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LEX_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_READ_ONLY")
    def AMAZON_LEX_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LEX_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_RUN_BOTS_ONLY")
    def AMAZON_LEX_RUN_BOTS_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LEX_RUN_BOTS_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_EQUIPMENT_FULL_ACCESS")
    def AMAZON_LOOKOUT_EQUIPMENT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_EQUIPMENT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_EQUIPMENT_READ_ONLY_ACCESS")
    def AMAZON_LOOKOUT_EQUIPMENT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_EQUIPMENT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_METRICS_FULL_ACCESS")
    def AMAZON_LOOKOUT_METRICS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_METRICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_METRICS_READ_ONLY_ACCESS")
    def AMAZON_LOOKOUT_METRICS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_METRICS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_VISION_CONSOLE_FULL_ACCESS")
    def AMAZON_LOOKOUT_VISION_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_VISION_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_VISION_CONSOLE_READ_ONLY_ACCESS")
    def AMAZON_LOOKOUT_VISION_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_VISION_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_VISION_FULL_ACCESS")
    def AMAZON_LOOKOUT_VISION_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_VISION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LOOKOUT_VISION_READ_ONLY_ACCESS")
    def AMAZON_LOOKOUT_VISION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_LOOKOUT_VISION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS")
    def AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_FULL_ACCESS")
    def AMAZON_MACHINE_LEARNING_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_FULL_ACCESS")
    def AMAZON_MACIE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACIE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_READ_ONLY_ACCESS")
    def AMAZON_MACIE_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MACIE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MCS_FULL_ACCESS")
    def AMAZON_MCS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MCS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MCS_READ_ONLY_ACCESS")
    def AMAZON_MCS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MCS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MECHANICAL_TURK_FULL_ACCESS")
    def AMAZON_MECHANICAL_TURK_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MECHANICAL_TURK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MECHANICAL_TURK_READ_ONLY")
    def AMAZON_MECHANICAL_TURK_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MECHANICAL_TURK_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MEMORY_DB_FULL_ACCESS")
    def AMAZON_MEMORY_DB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MEMORY_DB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MEMORY_DB_READ_ONLY_ACCESS")
    def AMAZON_MEMORY_DB_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MEMORY_DB_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_FULL_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MONITRON_FULL_ACCESS")
    def AMAZON_MONITRON_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MONITRON_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_API_FULL_ACCESS")
    def AMAZON_MQ_API_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MQ_API_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_API_READ_ONLY_ACCESS")
    def AMAZON_MQ_API_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MQ_API_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_FULL_ACCESS")
    def AMAZON_MQ_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MQ_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_READ_ONLY_ACCESS")
    def AMAZON_MQ_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MQ_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MSK_CONNECT_READ_ONLY_ACCESS")
    def AMAZON_MSK_CONNECT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MSK_CONNECT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MSK_FULL_ACCESS")
    def AMAZON_MSK_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MSK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MSK_READ_ONLY_ACCESS")
    def AMAZON_MSK_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_MSK_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_NIMBLE_STUDIO_LAUNCH_PROFILE_WORKER")
    def AMAZON_NIMBLE_STUDIO_LAUNCH_PROFILE_WORKER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_NIMBLE_STUDIO_LAUNCH_PROFILE_WORKER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_NIMBLE_STUDIO_STUDIO_ADMIN")
    def AMAZON_NIMBLE_STUDIO_STUDIO_ADMIN(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_NIMBLE_STUDIO_STUDIO_ADMIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_NIMBLE_STUDIO_STUDIO_USER")
    def AMAZON_NIMBLE_STUDIO_STUDIO_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_NIMBLE_STUDIO_STUDIO_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OMICS_FULL_ACCESS")
    def AMAZON_OMICS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OMICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OMICS_READ_ONLY_ACCESS")
    def AMAZON_OMICS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OMICS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ONE_ENTERPRISE_FULL_ACCESS")
    def AMAZON_ONE_ENTERPRISE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ONE_ENTERPRISE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ONE_ENTERPRISE_INSTALLER_ACCESS")
    def AMAZON_ONE_ENTERPRISE_INSTALLER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ONE_ENTERPRISE_INSTALLER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ONE_ENTERPRISE_READ_ONLY_ACCESS")
    def AMAZON_ONE_ENTERPRISE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ONE_ENTERPRISE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_DIRECT_QUERY_GLUE_CREATE_ACCESS")
    def AMAZON_OPEN_SEARCH_DIRECT_QUERY_GLUE_CREATE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_DIRECT_QUERY_GLUE_CREATE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_INGESTION_FULL_ACCESS")
    def AMAZON_OPEN_SEARCH_INGESTION_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_INGESTION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_INGESTION_READ_ONLY_ACCESS")
    def AMAZON_OPEN_SEARCH_INGESTION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_INGESTION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_SERVICE_COGNITO_ACCESS")
    def AMAZON_OPEN_SEARCH_SERVICE_COGNITO_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_SERVICE_COGNITO_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_SERVICE_FULL_ACCESS")
    def AMAZON_OPEN_SEARCH_SERVICE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_SERVICE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_OPEN_SEARCH_SERVICE_READ_ONLY_ACCESS")
    def AMAZON_OPEN_SEARCH_SERVICE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_OPEN_SEARCH_SERVICE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_POLLY_FULL_ACCESS")
    def AMAZON_POLLY_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_POLLY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_POLLY_READ_ONLY_ACCESS")
    def AMAZON_POLLY_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_POLLY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PROMETHEUS_CONSOLE_FULL_ACCESS")
    def AMAZON_PROMETHEUS_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_PROMETHEUS_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PROMETHEUS_FULL_ACCESS")
    def AMAZON_PROMETHEUS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_PROMETHEUS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PROMETHEUS_QUERY_ACCESS")
    def AMAZON_PROMETHEUS_QUERY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_PROMETHEUS_QUERY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PROMETHEUS_REMOTE_WRITE_ACCESS")
    def AMAZON_PROMETHEUS_REMOTE_WRITE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_PROMETHEUS_REMOTE_WRITE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_Q_DEVELOPER_ACCESS")
    def AMAZON_Q_DEVELOPER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_Q_DEVELOPER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_Q_FULL_ACCESS")
    def AMAZON_Q_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_Q_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_CONSOLE_FULL_ACCESS")
    def AMAZON_QLDB_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_QLDB_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_FULL_ACCESS")
    def AMAZON_QLDB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_QLDB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_READ_ONLY")
    def AMAZON_QLDB_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_QLDB_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_CUSTOM_INSTANCE_PROFILE_ROLE_POLICY")
    def AMAZON_RDS_CUSTOM_INSTANCE_PROFILE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_CUSTOM_INSTANCE_PROFILE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_DATA_FULL_ACCESS")
    def AMAZON_RDS_DATA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_DATA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_FULL_ACCESS")
    def AMAZON_RDS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_PERFORMANCE_INSIGHTS_FULL_ACCESS")
    def AMAZON_RDS_PERFORMANCE_INSIGHTS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_PERFORMANCE_INSIGHTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_PERFORMANCE_INSIGHTS_READ_ONLY")
    def AMAZON_RDS_PERFORMANCE_INSIGHTS_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_PERFORMANCE_INSIGHTS_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_READ_ONLY_ACCESS")
    def AMAZON_RDS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_RDS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_ALL_COMMANDS_FULL_ACCESS")
    def AMAZON_REDSHIFT_ALL_COMMANDS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_ALL_COMMANDS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_DATA_FULL_ACCESS")
    def AMAZON_REDSHIFT_DATA_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_DATA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_FULL_ACCESS")
    def AMAZON_REDSHIFT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR")
    def AMAZON_REDSHIFT_QUERY_EDITOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR_V2_FULL_ACCESS")
    def AMAZON_REDSHIFT_QUERY_EDITOR_V2_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR_V2_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR_V2_NO_SHARING")
    def AMAZON_REDSHIFT_QUERY_EDITOR_V2_NO_SHARING(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR_V2_NO_SHARING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_SHARING")
    def AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_SHARING(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_SHARING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_WRITE_SHARING")
    def AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_WRITE_SHARING(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR_V2_READ_WRITE_SHARING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_READ_ONLY_ACCESS")
    def AMAZON_REDSHIFT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REDSHIFT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_CUSTOM_LABELS_FULL_ACCESS")
    def AMAZON_REKOGNITION_CUSTOM_LABELS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REKOGNITION_CUSTOM_LABELS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_FULL_ACCESS")
    def AMAZON_REKOGNITION_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REKOGNITION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_READ_ONLY_ACCESS")
    def AMAZON_REKOGNITION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_REKOGNITION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_AUTO_NAMING_FULL_ACCESS")
    def AMAZON_ROUTE53_AUTO_NAMING_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_AUTO_NAMING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_AUTO_NAMING_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_AUTO_NAMING_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_AUTO_NAMING_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_AUTO_NAMING_REGISTRANT_ACCESS")
    def AMAZON_ROUTE53_AUTO_NAMING_REGISTRANT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_AUTO_NAMING_REGISTRANT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_DOMAINS_FULL_ACCESS")
    def AMAZON_ROUTE53_DOMAINS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_DOMAINS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_DOMAINS_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_DOMAINS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_DOMAINS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_FULL_ACCESS")
    def AMAZON_ROUTE53_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_PROFILES_FULL_ACCESS")
    def AMAZON_ROUTE53_PROFILES_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_PROFILES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_PROFILES_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_PROFILES_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_PROFILES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_CLUSTER_FULL_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_CLUSTER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_CLUSTER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_CLUSTER_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_CLUSTER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_CLUSTER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_FULL_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_CONTROL_CONFIG_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_READINESS_FULL_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_READINESS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_READINESS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RECOVERY_READINESS_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_RECOVERY_READINESS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RECOVERY_READINESS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RESOLVER_FULL_ACCESS")
    def AMAZON_ROUTE53_RESOLVER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RESOLVER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE53_RESOLVER_READ_ONLY_ACCESS")
    def AMAZON_ROUTE53_RESOLVER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ROUTE53_RESOLVER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_FULL_ACCESS")
    def AMAZON_S3_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_OUTPOSTS_FULL_ACCESS")
    def AMAZON_S3_OUTPOSTS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_OUTPOSTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_OUTPOSTS_READ_ONLY_ACCESS")
    def AMAZON_S3_OUTPOSTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_OUTPOSTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_READ_ONLY_ACCESS")
    def AMAZON_S3_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_TABLES_FULL_ACCESS")
    def AMAZON_S3_TABLES_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_TABLES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_TABLES_READ_ONLY_ACCESS")
    def AMAZON_S3_TABLES_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_S3_TABLES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_ADMIN_SERVICE_CATALOG_PRODUCTS_SERVICE_ROLE_POLICY")
    def AMAZON_SAGE_MAKER_ADMIN_SERVICE_CATALOG_PRODUCTS_SERVICE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_ADMIN_SERVICE_CATALOG_PRODUCTS_SERVICE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_AI_SERVICES_ACCESS")
    def AMAZON_SAGE_MAKER_CANVAS_AI_SERVICES_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_AI_SERVICES_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_BEDROCK_ACCESS")
    def AMAZON_SAGE_MAKER_CANVAS_BEDROCK_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_BEDROCK_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_DATA_PREP_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_CANVAS_DATA_PREP_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_DATA_PREP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_EMR_SERVERLESS_EXECUTION_ROLE_POLICY")
    def AMAZON_SAGE_MAKER_CANVAS_EMR_SERVERLESS_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_EMR_SERVERLESS_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_CANVAS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CANVAS_SM_DATA_SCIENCE_ASSISTANT_ACCESS")
    def AMAZON_SAGE_MAKER_CANVAS_SM_DATA_SCIENCE_ASSISTANT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CANVAS_SM_DATA_SCIENCE_ASSISTANT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_CLUSTER_INSTANCE_ROLE_POLICY")
    def AMAZON_SAGE_MAKER_CLUSTER_INSTANCE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_CLUSTER_INSTANCE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_FEATURE_STORE_ACCESS")
    def AMAZON_SAGE_MAKER_FEATURE_STORE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_FEATURE_STORE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_GROUND_TRUTH_EXECUTION")
    def AMAZON_SAGE_MAKER_GROUND_TRUTH_EXECUTION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_GROUND_TRUTH_EXECUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS")
    def AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_MODEL_GOVERNANCE_USE_ACCESS")
    def AMAZON_SAGE_MAKER_MODEL_GOVERNANCE_USE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_MODEL_GOVERNANCE_USE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_MODEL_REGISTRY_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_MODEL_REGISTRY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_MODEL_REGISTRY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_PARTNER_APPS_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_PARTNER_APPS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_PARTNER_APPS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_PIPELINES_INTEGRATIONS")
    def AMAZON_SAGE_MAKER_PIPELINES_INTEGRATIONS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_PIPELINES_INTEGRATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_READ_ONLY")
    def AMAZON_SAGE_MAKER_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_SERVICE_CATALOG_PRODUCTS_CODE_BUILD_SERVICE_ROLE_POLICY")
    def AMAZON_SAGE_MAKER_SERVICE_CATALOG_PRODUCTS_CODE_BUILD_SERVICE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_SERVICE_CATALOG_PRODUCTS_CODE_BUILD_SERVICE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_TRAINING_PLAN_CREATE_ACCESS")
    def AMAZON_SAGE_MAKER_TRAINING_PLAN_CREATE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SAGE_MAKER_TRAINING_PLAN_CREATE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SECURITY_LAKE_ADMINISTRATOR")
    def AMAZON_SECURITY_LAKE_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SECURITY_LAKE_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SECURITY_LAKE_PERMISSIONS_BOUNDARY")
    def AMAZON_SECURITY_LAKE_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SECURITY_LAKE_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SES_FULL_ACCESS")
    def AMAZON_SES_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SES_READ_ONLY_ACCESS")
    def AMAZON_SES_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SES_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS_FULL_ACCESS")
    def AMAZON_SNS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SNS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS_READ_ONLY_ACCESS")
    def AMAZON_SNS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SNS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SQS_FULL_ACCESS")
    def AMAZON_SQS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SQS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SQS_READ_ONLY_ACCESS")
    def AMAZON_SQS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SQS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_AUTOMATION_APPROVER_ACCESS")
    def AMAZON_SSM_AUTOMATION_APPROVER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_AUTOMATION_APPROVER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_DIRECTORY_SERVICE_ACCESS")
    def AMAZON_SSM_DIRECTORY_SERVICE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_DIRECTORY_SERVICE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_FULL_ACCESS")
    def AMAZON_SSM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_MANAGED_EC2_INSTANCE_DEFAULT_POLICY")
    def AMAZON_SSM_MANAGED_EC2_INSTANCE_DEFAULT_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_MANAGED_EC2_INSTANCE_DEFAULT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_MANAGED_INSTANCE_CORE")
    def AMAZON_SSM_MANAGED_INSTANCE_CORE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_MANAGED_INSTANCE_CORE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_PATCH_ASSOCIATION")
    def AMAZON_SSM_PATCH_ASSOCIATION(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_PATCH_ASSOCIATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_READ_ONLY_ACCESS")
    def AMAZON_SSM_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_SSM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TEXTRACT_FULL_ACCESS")
    def AMAZON_TEXTRACT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TEXTRACT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TIMESTREAM_CONSOLE_FULL_ACCESS")
    def AMAZON_TIMESTREAM_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TIMESTREAM_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TIMESTREAM_FULL_ACCESS")
    def AMAZON_TIMESTREAM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TIMESTREAM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TIMESTREAM_INFLUX_DB_FULL_ACCESS")
    def AMAZON_TIMESTREAM_INFLUX_DB_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TIMESTREAM_INFLUX_DB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TIMESTREAM_READ_ONLY_ACCESS")
    def AMAZON_TIMESTREAM_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TIMESTREAM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSCRIBE_FULL_ACCESS")
    def AMAZON_TRANSCRIBE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TRANSCRIBE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSCRIBE_READ_ONLY_ACCESS")
    def AMAZON_TRANSCRIBE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_TRANSCRIBE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VERIFIED_PERMISSIONS_FULL_ACCESS")
    def AMAZON_VERIFIED_PERMISSIONS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VERIFIED_PERMISSIONS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VERIFIED_PERMISSIONS_READ_ONLY_ACCESS")
    def AMAZON_VERIFIED_PERMISSIONS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VERIFIED_PERMISSIONS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS")
    def AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_FULL_ACCESS")
    def AMAZON_VPC_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_NETWORK_ACCESS_ANALYZER_FULL_ACCESS_POLICY")
    def AMAZON_VPC_NETWORK_ACCESS_ANALYZER_FULL_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_NETWORK_ACCESS_ANALYZER_FULL_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_REACHABILITY_ANALYZER_FULL_ACCESS_POLICY")
    def AMAZON_VPC_REACHABILITY_ANALYZER_FULL_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_REACHABILITY_ANALYZER_FULL_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_REACHABILITY_ANALYZER_PATH_COMPONENT_READ_POLICY")
    def AMAZON_VPC_REACHABILITY_ANALYZER_PATH_COMPONENT_READ_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_REACHABILITY_ANALYZER_PATH_COMPONENT_READ_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_READ_ONLY_ACCESS")
    def AMAZON_VPC_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_VPC_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_DOCS_FULL_ACCESS")
    def AMAZON_WORK_DOCS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_DOCS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_DOCS_READ_ONLY_ACCESS")
    def AMAZON_WORK_DOCS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_DOCS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_FULL_ACCESS")
    def AMAZON_WORK_MAIL_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_MAIL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_MESSAGE_FLOW_FULL_ACCESS")
    def AMAZON_WORK_MAIL_MESSAGE_FLOW_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_MAIL_MESSAGE_FLOW_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_MESSAGE_FLOW_READ_ONLY_ACCESS")
    def AMAZON_WORK_MAIL_MESSAGE_FLOW_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_MAIL_MESSAGE_FLOW_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_READ_ONLY_ACCESS")
    def AMAZON_WORK_MAIL_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_MAIL_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_ADMIN")
    def AMAZON_WORK_SPACES_ADMIN(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_ADMIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS")
    def AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_POOL_SERVICE_ACCESS")
    def AMAZON_WORK_SPACES_POOL_SERVICE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_POOL_SERVICE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_SECURE_BROWSER_READ_ONLY")
    def AMAZON_WORK_SPACES_SECURE_BROWSER_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_SECURE_BROWSER_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS")
    def AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_SERVICE_ACCESS")
    def AMAZON_WORK_SPACES_SERVICE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_SERVICE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_THIN_CLIENT_FULL_ACCESS")
    def AMAZON_WORK_SPACES_THIN_CLIENT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_THIN_CLIENT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_THIN_CLIENT_READ_ONLY_ACCESS")
    def AMAZON_WORK_SPACES_THIN_CLIENT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_THIN_CLIENT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_WEB_READ_ONLY")
    def AMAZON_WORK_SPACES_WEB_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORK_SPACES_WEB_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORKSPACES_PCA_ACCESS")
    def AMAZON_WORKSPACES_PCA_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_WORKSPACES_PCA_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ZOCALO_FULL_ACCESS")
    def AMAZON_ZOCALO_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ZOCALO_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ZOCALO_READ_ONLY_ACCESS")
    def AMAZON_ZOCALO_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AMAZON_ZOCALO_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_CONSOLE_FULL_ACCESS")
    def AUTO_SCALING_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AUTO_SCALING_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS")
    def AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_FULL_ACCESS")
    def AUTO_SCALING_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AUTO_SCALING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_READ_ONLY_ACCESS")
    def AUTO_SCALING_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AUTO_SCALING_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_ACTIVITY_ACCESS")
    def AWS_ACCOUNT_ACTIVITY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ACCOUNT_ACTIVITY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_MANAGEMENT_FULL_ACCESS")
    def AWS_ACCOUNT_MANAGEMENT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ACCOUNT_MANAGEMENT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_MANAGEMENT_READ_ONLY_ACCESS")
    def AWS_ACCOUNT_MANAGEMENT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ACCOUNT_MANAGEMENT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_USAGE_REPORT_ACCESS")
    def AWS_ACCOUNT_USAGE_REPORT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ACCOUNT_USAGE_REPORT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AGENTLESS_DISCOVERY_SERVICE")
    def AWS_AGENTLESS_DISCOVERY_SERVICE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_AGENTLESS_DISCOVERY_SERVICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_FABRIC_FULL_ACCESS")
    def AWS_APP_FABRIC_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_FABRIC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_FABRIC_READ_ONLY_ACCESS")
    def AWS_APP_FABRIC_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_FABRIC_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_ENVOY_ACCESS")
    def AWS_APP_MESH_ENVOY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_MESH_ENVOY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_FULL_ACCESS")
    def AWS_APP_MESH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_MESH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_PREVIEW_ENVOY_ACCESS")
    def AWS_APP_MESH_PREVIEW_ENVOY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_MESH_PREVIEW_ENVOY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_READ_ONLY")
    def AWS_APP_MESH_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_MESH_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_RUNNER_FULL_ACCESS")
    def AWS_APP_RUNNER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_RUNNER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_RUNNER_READ_ONLY_ACCESS")
    def AWS_APP_RUNNER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_RUNNER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_ADMINISTRATOR")
    def AWS_APP_SYNC_ADMINISTRATOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_SYNC_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_INVOKE_FULL_ACCESS")
    def AWS_APP_SYNC_INVOKE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_SYNC_INVOKE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_SCHEMA_AUTHOR")
    def AWS_APP_SYNC_SCHEMA_AUTHOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APP_SYNC_SCHEMA_AUTHOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_DISCOVERY_AGENT_ACCESS")
    def AWS_APPLICATION_DISCOVERY_AGENT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_DISCOVERY_AGENT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_DISCOVERY_AGENTLESS_COLLECTOR_ACCESS")
    def AWS_APPLICATION_DISCOVERY_AGENTLESS_COLLECTOR_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_DISCOVERY_AGENTLESS_COLLECTOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS")
    def AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_AGENT_INSTALLATION_POLICY")
    def AWS_APPLICATION_MIGRATION_AGENT_INSTALLATION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_AGENT_INSTALLATION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_AGENT_POLICY")
    def AWS_APPLICATION_MIGRATION_AGENT_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_AGENT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_EC2_ACCESS")
    def AWS_APPLICATION_MIGRATION_EC2_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_EC2_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_FULL_ACCESS")
    def AWS_APPLICATION_MIGRATION_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_READ_ONLY_ACCESS")
    def AWS_APPLICATION_MIGRATION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_SERVICE_EC2_INSTANCE_POLICY")
    def AWS_APPLICATION_MIGRATION_SERVICE_EC2_INSTANCE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_SERVICE_EC2_INSTANCE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_SSM_ACCESS")
    def AWS_APPLICATION_MIGRATION_SSM_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_SSM_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_MIGRATION_V_CENTER_CLIENT_POLICY")
    def AWS_APPLICATION_MIGRATION_V_CENTER_CLIENT_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_APPLICATION_MIGRATION_V_CENTER_CLIENT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ARTIFACT_AGREEMENTS_FULL_ACCESS")
    def AWS_ARTIFACT_AGREEMENTS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ARTIFACT_AGREEMENTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ARTIFACT_AGREEMENTS_READ_ONLY_ACCESS")
    def AWS_ARTIFACT_AGREEMENTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ARTIFACT_AGREEMENTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ARTIFACT_REPORTS_READ_ONLY_ACCESS")
    def AWS_ARTIFACT_REPORTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ARTIFACT_REPORTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AUDIT_MANAGER_ADMINISTRATOR_ACCESS")
    def AWS_AUDIT_MANAGER_ADMINISTRATOR_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_AUDIT_MANAGER_ADMINISTRATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_AUDIT_ACCESS")
    def AWS_BACKUP_AUDIT_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_AUDIT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_DATA_TRANSFER_ACCESS")
    def AWS_BACKUP_DATA_TRANSFER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_DATA_TRANSFER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_FULL_ACCESS")
    def AWS_BACKUP_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_OPERATOR_ACCESS")
    def AWS_BACKUP_OPERATOR_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_OPERATOR_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_ORGANIZATION_ADMIN_ACCESS")
    def AWS_BACKUP_ORGANIZATION_ADMIN_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_ORGANIZATION_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_RESTORE_ACCESS_FOR_SAPHANA")
    def AWS_BACKUP_RESTORE_ACCESS_FOR_SAPHANA(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_RESTORE_ACCESS_FOR_SAPHANA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_INDEXING")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_INDEXING(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_INDEXING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_ITEM_RESTORES")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_ITEM_RESTORES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_ITEM_RESTORES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_BACKUP")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_BACKUP(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_BACKUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_RESTORE")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_RESTORE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_S3_RESTORE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BATCH_FULL_ACCESS")
    def AWS_BATCH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BATCH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BILLING_CONDUCTOR_FULL_ACCESS")
    def AWS_BILLING_CONDUCTOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BILLING_CONDUCTOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BILLING_CONDUCTOR_READ_ONLY_ACCESS")
    def AWS_BILLING_CONDUCTOR_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BILLING_CONDUCTOR_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BILLING_READ_ONLY_ACCESS")
    def AWS_BILLING_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BILLING_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUDGETS_ACTIONS_ROLE_POLICY_FOR_RESOURCE_ADMINISTRATION_WITH_SSM")
    def AWS_BUDGETS_ACTIONS_ROLE_POLICY_FOR_RESOURCE_ADMINISTRATION_WITH_SSM(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BUDGETS_ACTIONS_ROLE_POLICY_FOR_RESOURCE_ADMINISTRATION_WITH_SSM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUDGETS_ACTIONS_WITH_AWS_RESOURCE_CONTROL_ACCESS")
    def AWS_BUDGETS_ACTIONS_WITH_AWS_RESOURCE_CONTROL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BUDGETS_ACTIONS_WITH_AWS_RESOURCE_CONTROL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUDGETS_READ_ONLY_ACCESS")
    def AWS_BUDGETS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BUDGETS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUG_BUST_FULL_ACCESS")
    def AWS_BUG_BUST_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BUG_BUST_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUG_BUST_PLAYER_ACCESS")
    def AWS_BUG_BUST_PLAYER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_BUG_BUST_PLAYER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_FULL_ACCESS")
    def AWS_CERTIFICATE_MANAGER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_READ_ONLY")
    def AWS_CERTIFICATE_MANAGER_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLEAN_ROOMS_FULL_ACCESS")
    def AWS_CLEAN_ROOMS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLEAN_ROOMS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLEAN_ROOMS_FULL_ACCESS_NO_QUERYING")
    def AWS_CLEAN_ROOMS_FULL_ACCESS_NO_QUERYING(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLEAN_ROOMS_FULL_ACCESS_NO_QUERYING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLEAN_ROOMS_ML_FULL_ACCESS")
    def AWS_CLEAN_ROOMS_ML_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLEAN_ROOMS_ML_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLEAN_ROOMS_ML_READ_ONLY_ACCESS")
    def AWS_CLEAN_ROOMS_ML_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLEAN_ROOMS_ML_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLEAN_ROOMS_READ_ONLY_ACCESS")
    def AWS_CLEAN_ROOMS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLEAN_ROOMS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FORMATION_FULL_ACCESS")
    def AWS_CLOUD_FORMATION_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_FORMATION_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FORMATION_READ_ONLY_ACCESS")
    def AWS_CLOUD_FORMATION_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_FORMATION_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM_FULL_ACCESS")
    def AWS_CLOUD_HSM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_HSM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM_READ_ONLY_ACCESS")
    def AWS_CLOUD_HSM_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_HSM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS")
    def AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_FULL_ACCESS")
    def AWS_CLOUD_MAP_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_MAP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_READ_ONLY_ACCESS")
    def AWS_CLOUD_MAP_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_MAP_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS")
    def AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_SHELL_FULL_ACCESS")
    def AWS_CLOUD_SHELL_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_SHELL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_TRAIL_FULL_ACCESS")
    def AWS_CLOUD_TRAIL_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_TRAIL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_TRAIL_READ_ONLY_ACCESS")
    def AWS_CLOUD_TRAIL_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD_TRAIL_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD9_ADMINISTRATOR")
    def AWS_CLOUD9_ADMINISTRATOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD9_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD9_ENVIRONMENT_MEMBER")
    def AWS_CLOUD9_ENVIRONMENT_MEMBER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD9_ENVIRONMENT_MEMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD9_SSM_INSTANCE_PROFILE")
    def AWS_CLOUD9_SSM_INSTANCE_PROFILE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD9_SSM_INSTANCE_PROFILE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD9_USER")
    def AWS_CLOUD9_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CLOUD9_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_ARTIFACT_ADMIN_ACCESS")
    def AWS_CODE_ARTIFACT_ADMIN_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_ARTIFACT_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_ARTIFACT_READ_ONLY_ACCESS")
    def AWS_CODE_ARTIFACT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_ARTIFACT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_ADMIN_ACCESS")
    def AWS_CODE_BUILD_ADMIN_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_BUILD_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_DEVELOPER_ACCESS")
    def AWS_CODE_BUILD_DEVELOPER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_BUILD_DEVELOPER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_READ_ONLY_ACCESS")
    def AWS_CODE_BUILD_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_BUILD_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_FULL_ACCESS")
    def AWS_CODE_COMMIT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_COMMIT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_POWER_USER")
    def AWS_CODE_COMMIT_POWER_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_COMMIT_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_READ_ONLY")
    def AWS_CODE_COMMIT_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_COMMIT_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_DEPLOYER_ACCESS")
    def AWS_CODE_DEPLOY_DEPLOYER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_DEPLOY_DEPLOYER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_FULL_ACCESS")
    def AWS_CODE_DEPLOY_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_DEPLOY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_READ_ONLY_ACCESS")
    def AWS_CODE_DEPLOY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_DEPLOY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE_FOR_ECS")
    def AWS_CODE_DEPLOY_ROLE_FOR_ECS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE_FOR_ECS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED")
    def AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_APPROVER_ACCESS")
    def AWS_CODE_PIPELINE_APPROVER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_PIPELINE_APPROVER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS")
    def AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_FULL_ACCESS")
    def AWS_CODE_PIPELINE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_PIPELINE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_READ_ONLY_ACCESS")
    def AWS_CODE_PIPELINE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_PIPELINE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR_FULL_ACCESS")
    def AWS_CODE_STAR_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CODE_STAR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_COMPROMISED_KEY_QUARANTINE")
    def AWS_COMPROMISED_KEY_QUARANTINE(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_COMPROMISED_KEY_QUARANTINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_COMPROMISED_KEY_QUARANTINE_V2")
    def AWS_COMPROMISED_KEY_QUARANTINE_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_COMPROMISED_KEY_QUARANTINE_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_COMPROMISED_KEY_QUARANTINE_V3")
    def AWS_COMPROMISED_KEY_QUARANTINE_V3(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_COMPROMISED_KEY_QUARANTINE_V3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_USER_ACCESS")
    def AWS_CONFIG_USER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CONFIG_USER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONNECTOR")
    def AWS_CONNECTOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_CONNECTOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_DATA_GRANT_OWNER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_DATA_GRANT_OWNER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_DATA_GRANT_OWNER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_DATA_GRANT_RECEIVER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_DATA_GRANT_RECEIVER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_DATA_GRANT_RECEIVER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_READ_ONLY")
    def AWS_DATA_EXCHANGE_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_PIPELINE_FULL_ACCESS")
    def AWS_DATA_PIPELINE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_PIPELINE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_PIPELINE_POWER_USER")
    def AWS_DATA_PIPELINE_POWER_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_PIPELINE_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_SYNC_FULL_ACCESS")
    def AWS_DATA_SYNC_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_SYNC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_SYNC_READ_ONLY_ACCESS")
    def AWS_DATA_SYNC_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DATA_SYNC_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_FLEET_WORKER")
    def AWS_DEADLINE_CLOUD_FLEET_WORKER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_FLEET_WORKER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_USER_ACCESS_FARMS")
    def AWS_DEADLINE_CLOUD_USER_ACCESS_FARMS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_USER_ACCESS_FARMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_USER_ACCESS_FLEETS")
    def AWS_DEADLINE_CLOUD_USER_ACCESS_FLEETS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_USER_ACCESS_FLEETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_USER_ACCESS_JOBS")
    def AWS_DEADLINE_CLOUD_USER_ACCESS_JOBS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_USER_ACCESS_JOBS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_USER_ACCESS_QUEUES")
    def AWS_DEADLINE_CLOUD_USER_ACCESS_QUEUES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_USER_ACCESS_QUEUES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEADLINE_CLOUD_WORKER_HOST")
    def AWS_DEADLINE_CLOUD_WORKER_HOST(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEADLINE_CLOUD_WORKER_HOST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY")
    def AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_ACCOUNT_ADMIN_ACCESS")
    def AWS_DEEP_RACER_ACCOUNT_ADMIN_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_RACER_ACCOUNT_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY")
    def AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_DEFAULT_MULTI_USER_ACCESS")
    def AWS_DEEP_RACER_DEFAULT_MULTI_USER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_RACER_DEFAULT_MULTI_USER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_FULL_ACCESS")
    def AWS_DEEP_RACER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_RACER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY")
    def AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DENY_ALL")
    def AWS_DENY_ALL(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DENY_ALL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEVICE_FARM_FULL_ACCESS")
    def AWS_DEVICE_FARM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DEVICE_FARM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECT_CONNECT_FULL_ACCESS")
    def AWS_DIRECT_CONNECT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECT_CONNECT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECT_CONNECT_READ_ONLY_ACCESS")
    def AWS_DIRECT_CONNECT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECT_CONNECT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_DATA_FULL_ACCESS")
    def AWS_DIRECTORY_SERVICE_DATA_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECTORY_SERVICE_DATA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_DATA_READ_ONLY_ACCESS")
    def AWS_DIRECTORY_SERVICE_DATA_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECTORY_SERVICE_DATA_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_FULL_ACCESS")
    def AWS_DIRECTORY_SERVICE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECTORY_SERVICE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS")
    def AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY")
    def AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_EC2_VSS_SNAPSHOT_POLICY")
    def AWS_EC2_VSS_SNAPSHOT_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_EC2_VSS_SNAPSHOT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE")
    def AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_CUSTOMER_ROLE_POLICY")
    def AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_CUSTOMER_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_CUSTOMER_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER")
    def AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_READ_ONLY")
    def AWS_ELASTIC_BEANSTALK_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_WEB_TIER")
    def AWS_ELASTIC_BEANSTALK_WEB_TIER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_WEB_TIER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_WORKER_TIER")
    def AWS_ELASTIC_BEANSTALK_WORKER_TIER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_WORKER_TIER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_AGENT_INSTALLATION_POLICY")
    def AWS_ELASTIC_DISASTER_RECOVERY_AGENT_INSTALLATION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_AGENT_INSTALLATION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS")
    def AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS_V2")
    def AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_CONSOLE_FULL_ACCESS_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_FAILBACK_INSTALLATION_POLICY")
    def AWS_ELASTIC_DISASTER_RECOVERY_FAILBACK_INSTALLATION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_FAILBACK_INSTALLATION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_LAUNCH_ACTIONS_POLICY")
    def AWS_ELASTIC_DISASTER_RECOVERY_LAUNCH_ACTIONS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_LAUNCH_ACTIONS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_DISASTER_RECOVERY_READ_ONLY_ACCESS")
    def AWS_ELASTIC_DISASTER_RECOVERY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELASTIC_DISASTER_RECOVERY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_LIVE_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_LIVE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_LIVE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_LIVE_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_LIVE_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_LIVE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_V2_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_V2_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_V2_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_V2_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_V2_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_V2_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_TAILOR_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_TAILOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_TAILOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_TAILOR_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_TAILOR_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_TAILOR_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ENTITY_RESOLUTION_CONSOLE_FULL_ACCESS")
    def AWS_ENTITY_RESOLUTION_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ENTITY_RESOLUTION_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ENTITY_RESOLUTION_CONSOLE_READ_ONLY_ACCESS")
    def AWS_ENTITY_RESOLUTION_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ENTITY_RESOLUTION_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FM_ADMIN_FULL_ACCESS")
    def AWS_FM_ADMIN_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_FM_ADMIN_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FM_ADMIN_READ_ONLY_ACCESS")
    def AWS_FM_ADMIN_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_FM_ADMIN_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FM_MEMBER_READ_ONLY_ACCESS")
    def AWS_FM_MEMBER_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_FM_MEMBER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FOR_WORD_PRESS_PLUGIN_POLICY")
    def AWS_FOR_WORD_PRESS_PLUGIN_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_FOR_WORD_PRESS_PLUGIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_CONSOLE_FULL_ACCESS")
    def AWS_GLUE_CONSOLE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS")
    def AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_DATA_BREW_FULL_ACCESS_POLICY")
    def AWS_GLUE_DATA_BREW_FULL_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_DATA_BREW_FULL_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SCHEMA_REGISTRY_FULL_ACCESS")
    def AWS_GLUE_SCHEMA_REGISTRY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_SCHEMA_REGISTRY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SCHEMA_REGISTRY_READONLY_ACCESS")
    def AWS_GLUE_SCHEMA_REGISTRY_READONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_SCHEMA_REGISTRY_READONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SESSION_USER_RESTRICTED_NOTEBOOK_POLICY")
    def AWS_GLUE_SESSION_USER_RESTRICTED_NOTEBOOK_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_SESSION_USER_RESTRICTED_NOTEBOOK_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SESSION_USER_RESTRICTED_POLICY")
    def AWS_GLUE_SESSION_USER_RESTRICTED_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GLUE_SESSION_USER_RESTRICTED_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GRAFANA_ACCOUNT_ADMINISTRATOR")
    def AWS_GRAFANA_ACCOUNT_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GRAFANA_ACCOUNT_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GRAFANA_CONSOLE_READ_ONLY_ACCESS")
    def AWS_GRAFANA_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GRAFANA_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT")
    def AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT_V2")
    def AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT_V2(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GRAFANA_WORKSPACE_PERMISSION_MANAGEMENT_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GREENGRASS_FULL_ACCESS")
    def AWS_GREENGRASS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GREENGRASS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GREENGRASS_READ_ONLY_ACCESS")
    def AWS_GREENGRASS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GREENGRASS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GROUND_STATION_AGENT_INSTANCE_POLICY")
    def AWS_GROUND_STATION_AGENT_INSTANCE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_GROUND_STATION_AGENT_INSTANCE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_HEALTH_FULL_ACCESS")
    def AWS_HEALTH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_HEALTH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_HEALTH_IMAGING_FULL_ACCESS")
    def AWS_HEALTH_IMAGING_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_HEALTH_IMAGING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_HEALTH_IMAGING_READ_ONLY_ACCESS")
    def AWS_HEALTH_IMAGING_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_HEALTH_IMAGING_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IAM_IDENTITY_CENTER_ALLOW_LIST_FOR_IDENTITY_CONTEXT")
    def AWS_IAM_IDENTITY_CENTER_ALLOW_LIST_FOR_IDENTITY_CONTEXT(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IAM_IDENTITY_CENTER_ALLOW_LIST_FOR_IDENTITY_CONTEXT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IDENTITY_SYNC_FULL_ACCESS")
    def AWS_IDENTITY_SYNC_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IDENTITY_SYNC_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IDENTITY_SYNC_READ_ONLY_ACCESS")
    def AWS_IDENTITY_SYNC_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IDENTITY_SYNC_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMAGE_BUILDER_FULL_ACCESS")
    def AWS_IMAGE_BUILDER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IMAGE_BUILDER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMAGE_BUILDER_READ_ONLY_ACCESS")
    def AWS_IMAGE_BUILDER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IMAGE_BUILDER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMPORT_EXPORT_FULL_ACCESS")
    def AWS_IMPORT_EXPORT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IMPORT_EXPORT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMPORT_EXPORT_READ_ONLY_ACCESS")
    def AWS_IMPORT_EXPORT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IMPORT_EXPORT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_INCIDENT_MANAGER_INCIDENT_ACCESS_SERVICE_ROLE_POLICY")
    def AWS_INCIDENT_MANAGER_INCIDENT_ACCESS_SERVICE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_INCIDENT_MANAGER_INCIDENT_ACCESS_SERVICE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_INCIDENT_MANAGER_RESOLVER_ACCESS")
    def AWS_INCIDENT_MANAGER_RESOLVER_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_INCIDENT_MANAGER_RESOLVER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_ANALYTICS_FULL_ACCESS")
    def AWS_IO_T_ANALYTICS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_ANALYTICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_ANALYTICS_READ_ONLY_ACCESS")
    def AWS_IO_T_ANALYTICS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_ANALYTICS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_CONFIG_ACCESS")
    def AWS_IO_T_CONFIG_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_CONFIG_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_CONFIG_READ_ONLY_ACCESS")
    def AWS_IO_T_CONFIG_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_CONFIG_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_DATA_ACCESS")
    def AWS_IO_T_DATA_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_DATA_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_DEVICE_TESTER_FOR_FREE_RTOS_FULL_ACCESS")
    def AWS_IO_T_DEVICE_TESTER_FOR_FREE_RTOS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_DEVICE_TESTER_FOR_FREE_RTOS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_DEVICE_TESTER_FOR_GREENGRASS_FULL_ACCESS")
    def AWS_IO_T_DEVICE_TESTER_FOR_GREENGRASS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_DEVICE_TESTER_FOR_GREENGRASS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_EVENTS_FULL_ACCESS")
    def AWS_IO_T_EVENTS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_EVENTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_EVENTS_READ_ONLY_ACCESS")
    def AWS_IO_T_EVENTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_EVENTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_FULL_ACCESS")
    def AWS_IO_T_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_SITE_WISE_CONSOLE_FULL_ACCESS")
    def AWS_IO_T_SITE_WISE_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_SITE_WISE_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_SITE_WISE_FULL_ACCESS")
    def AWS_IO_T_SITE_WISE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_SITE_WISE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_SITE_WISE_READ_ONLY_ACCESS")
    def AWS_IO_T_SITE_WISE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_SITE_WISE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_DATA_ACCESS")
    def AWS_IO_T_WIRELESS_DATA_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_DATA_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_FULL_ACCESS")
    def AWS_IO_T_WIRELESS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_FULL_PUBLISH_ACCESS")
    def AWS_IO_T_WIRELESS_FULL_PUBLISH_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_FULL_PUBLISH_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_GATEWAY_CERT_MANAGER")
    def AWS_IO_T_WIRELESS_GATEWAY_CERT_MANAGER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_GATEWAY_CERT_MANAGER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_LOGGING")
    def AWS_IO_T_WIRELESS_LOGGING(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_LOGGING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T_WIRELESS_READ_ONLY_ACCESS")
    def AWS_IO_T_WIRELESS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T_WIRELESS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T1_CLICK_FULL_ACCESS")
    def AWS_IO_T1_CLICK_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T1_CLICK_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IO_T1_CLICK_READ_ONLY_ACCESS")
    def AWS_IO_T1_CLICK_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IO_T1_CLICK_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IQ_FULL_ACCESS")
    def AWS_IQ_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_IQ_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_KEY_MANAGEMENT_SERVICE_POWER_USER")
    def AWS_KEY_MANAGEMENT_SERVICE_POWER_USER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_KEY_MANAGEMENT_SERVICE_POWER_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAKE_FORMATION_CROSS_ACCOUNT_MANAGER")
    def AWS_LAKE_FORMATION_CROSS_ACCOUNT_MANAGER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAKE_FORMATION_CROSS_ACCOUNT_MANAGER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAKE_FORMATION_DATA_ADMIN")
    def AWS_LAKE_FORMATION_DATA_ADMIN(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAKE_FORMATION_DATA_ADMIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_EXECUTE")
    def AWS_LAMBDA_EXECUTE(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAMBDA_EXECUTE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_FULL_ACCESS")
    def AWS_LAMBDA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAMBDA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_INVOCATION_DYNAMO_DB")
    def AWS_LAMBDA_INVOCATION_DYNAMO_DB(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAMBDA_INVOCATION_DYNAMO_DB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_READ_ONLY_ACCESS")
    def AWS_LAMBDA_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_LAMBDA_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_AMI_INGESTION")
    def AWS_MARKETPLACE_AMI_INGESTION(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_AMI_INGESTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_FULL_ACCESS")
    def AWS_MARKETPLACE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_GET_ENTITLEMENTS")
    def AWS_MARKETPLACE_GET_ENTITLEMENTS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_GET_ENTITLEMENTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS")
    def AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS")
    def AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_METERING_FULL_ACCESS")
    def AWS_MARKETPLACE_METERING_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_METERING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_METERING_REGISTER_USAGE")
    def AWS_MARKETPLACE_METERING_REGISTER_USAGE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_METERING_REGISTER_USAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS")
    def AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_READ_ONLY")
    def AWS_MARKETPLACE_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_FULL_ACCESS")
    def AWS_MARKETPLACE_SELLER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_SELLER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_OFFER_MANAGEMENT")
    def AWS_MARKETPLACE_SELLER_OFFER_MANAGEMENT(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_SELLER_OFFER_MANAGEMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS")
    def AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY")
    def AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_FULL_ACCESS")
    def AWS_MIGRATION_HUB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_ORCHESTRATOR_CONSOLE_FULL_ACCESS")
    def AWS_MIGRATION_HUB_ORCHESTRATOR_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_ORCHESTRATOR_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_ORCHESTRATOR_INSTANCE_ROLE_POLICY")
    def AWS_MIGRATION_HUB_ORCHESTRATOR_INSTANCE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_ORCHESTRATOR_INSTANCE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_ORCHESTRATOR_PLUGIN")
    def AWS_MIGRATION_HUB_ORCHESTRATOR_PLUGIN(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_ORCHESTRATOR_PLUGIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_REFACTOR_SPACES_ENVIRONMENTS_WITHOUT_BRIDGES_FULL_ACCESS")
    def AWS_MIGRATION_HUB_REFACTOR_SPACES_ENVIRONMENTS_WITHOUT_BRIDGES_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_REFACTOR_SPACES_ENVIRONMENTS_WITHOUT_BRIDGES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_REFACTOR_SPACES_FULL_ACCESS")
    def AWS_MIGRATION_HUB_REFACTOR_SPACES_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_REFACTOR_SPACES_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_STRATEGY_COLLECTOR")
    def AWS_MIGRATION_HUB_STRATEGY_COLLECTOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_STRATEGY_COLLECTOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_STRATEGY_CONSOLE_FULL_ACCESS")
    def AWS_MIGRATION_HUB_STRATEGY_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_MIGRATION_HUB_STRATEGY_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_NETWORK_MANAGER_FULL_ACCESS")
    def AWS_NETWORK_MANAGER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_NETWORK_MANAGER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_NETWORK_MANAGER_READ_ONLY_ACCESS")
    def AWS_NETWORK_MANAGER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_NETWORK_MANAGER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CLOUD_WATCH_LOGS")
    def AWS_OPS_WORKS_CLOUD_WATCH_LOGS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_CLOUD_WATCH_LOGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE")
    def AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_FULL_ACCESS")
    def AWS_OPS_WORKS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_INSTANCE_REGISTRATION")
    def AWS_OPS_WORKS_INSTANCE_REGISTRATION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_INSTANCE_REGISTRATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_REGISTER_CLI_EC2")
    def AWS_OPS_WORKS_REGISTER_CLI_EC2(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_REGISTER_CLI_EC2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES")
    def AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS_FULL_ACCESS")
    def AWS_ORGANIZATIONS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ORGANIZATIONS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS_READ_ONLY_ACCESS")
    def AWS_ORGANIZATIONS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ORGANIZATIONS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OUTPOSTS_AUTHORIZE_SERVER_POLICY")
    def AWS_OUTPOSTS_AUTHORIZE_SERVER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_OUTPOSTS_AUTHORIZE_SERVER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PANORAMA_FULL_ACCESS")
    def AWS_PANORAMA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PANORAMA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PARTNER_CENTRAL_FULL_ACCESS")
    def AWS_PARTNER_CENTRAL_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PARTNER_CENTRAL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PARTNER_CENTRAL_OPPORTUNITY_MANAGEMENT")
    def AWS_PARTNER_CENTRAL_OPPORTUNITY_MANAGEMENT(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PARTNER_CENTRAL_OPPORTUNITY_MANAGEMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PARTNER_CENTRAL_SANDBOX_FULL_ACCESS")
    def AWS_PARTNER_CENTRAL_SANDBOX_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PARTNER_CENTRAL_SANDBOX_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PARTNER_CENTRAL_SELLING_RESOURCE_SNAPSHOT_JOB_EXECUTION_ROLE_POLICY")
    def AWS_PARTNER_CENTRAL_SELLING_RESOURCE_SNAPSHOT_JOB_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PARTNER_CENTRAL_SELLING_RESOURCE_SNAPSHOT_JOB_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PARTNER_LED_SUPPORT_READ_ONLY_ACCESS")
    def AWS_PARTNER_LED_SUPPORT_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PARTNER_LED_SUPPORT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRICE_LIST_SERVICE_FULL_ACCESS")
    def AWS_PRICE_LIST_SERVICE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRICE_LIST_SERVICE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_CA_AUDITOR")
    def AWS_PRIVATE_CA_AUDITOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_CA_AUDITOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_CA_FULL_ACCESS")
    def AWS_PRIVATE_CA_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_CA_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_CA_PRIVILEGED_USER")
    def AWS_PRIVATE_CA_PRIVILEGED_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_CA_PRIVILEGED_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_CA_READ_ONLY")
    def AWS_PRIVATE_CA_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_CA_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_CA_USER")
    def AWS_PRIVATE_CA_USER(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_CA_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS")
    def AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_MARKETPLACE_REQUESTS")
    def AWS_PRIVATE_MARKETPLACE_REQUESTS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PRIVATE_MARKETPLACE_REQUESTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PROTON_CODE_BUILD_PROVISIONING_BASIC_ACCESS")
    def AWS_PROTON_CODE_BUILD_PROVISIONING_BASIC_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PROTON_CODE_BUILD_PROVISIONING_BASIC_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PROTON_DEVELOPER_ACCESS")
    def AWS_PROTON_DEVELOPER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PROTON_DEVELOPER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PROTON_FULL_ACCESS")
    def AWS_PROTON_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PROTON_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PROTON_READ_ONLY_ACCESS")
    def AWS_PROTON_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PROTON_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PURCHASE_ORDERS_SERVICE_ROLE_POLICY")
    def AWS_PURCHASE_ORDERS_SERVICE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_PURCHASE_ORDERS_SERVICE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_CFGC_PACKS_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_CFGC_PACKS_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_CFGC_PACKS_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_DEPLOYMENT_ROLE_POLICY")
    def AWS_QUICK_SETUP_DEPLOYMENT_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_DEPLOYMENT_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_DEV_OPS_GURU_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_DEV_OPS_GURU_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_DEV_OPS_GURU_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_DISTRIBUTOR_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_DISTRIBUTOR_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_DISTRIBUTOR_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_ENABLE_AREX_EXECUTION_POLICY")
    def AWS_QUICK_SETUP_ENABLE_AREX_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_ENABLE_AREX_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_ENABLE_DHMC_EXECUTION_POLICY")
    def AWS_QUICK_SETUP_ENABLE_DHMC_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_ENABLE_DHMC_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_MANAGED_INSTANCE_PROFILE_EXECUTION_POLICY")
    def AWS_QUICK_SETUP_MANAGED_INSTANCE_PROFILE_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_MANAGED_INSTANCE_PROFILE_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_PATCH_POLICY_BASELINE_ACCESS")
    def AWS_QUICK_SETUP_PATCH_POLICY_BASELINE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_PATCH_POLICY_BASELINE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_PATCH_POLICY_DEPLOYMENT_ROLE_POLICY")
    def AWS_QUICK_SETUP_PATCH_POLICY_DEPLOYMENT_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_PATCH_POLICY_DEPLOYMENT_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_PATCH_POLICY_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_PATCH_POLICY_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_PATCH_POLICY_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SCHEDULER_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_SCHEDULER_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SCHEDULER_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SSM_DEPLOYMENT_ROLE_POLICY")
    def AWS_QUICK_SETUP_SSM_DEPLOYMENT_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SSM_DEPLOYMENT_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SSM_DEPLOYMENT_S3_BUCKET_ROLE_POLICY")
    def AWS_QUICK_SETUP_SSM_DEPLOYMENT_S3_BUCKET_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SSM_DEPLOYMENT_S3_BUCKET_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SSM_HOST_MGMT_PERMISSIONS_BOUNDARY")
    def AWS_QUICK_SETUP_SSM_HOST_MGMT_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SSM_HOST_MGMT_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SSM_LIFECYCLE_MANAGEMENT_EXECUTION_POLICY")
    def AWS_QUICK_SETUP_SSM_LIFECYCLE_MANAGEMENT_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SSM_LIFECYCLE_MANAGEMENT_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SETUP_SSM_MANAGE_RESOURCES_EXECUTION_POLICY")
    def AWS_QUICK_SETUP_SSM_MANAGE_RESOURCES_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SETUP_SSM_MANAGE_RESOURCES_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_ASSET_BUNDLE_EXPORT_POLICY")
    def AWS_QUICK_SIGHT_ASSET_BUNDLE_EXPORT_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SIGHT_ASSET_BUNDLE_EXPORT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_ASSET_BUNDLE_IMPORT_POLICY")
    def AWS_QUICK_SIGHT_ASSET_BUNDLE_IMPORT_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SIGHT_ASSET_BUNDLE_IMPORT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_IO_T_ANALYTICS_ACCESS")
    def AWS_QUICK_SIGHT_IO_T_ANALYTICS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_QUICK_SIGHT_IO_T_ANALYTICS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_REFACTORING_TOOLKIT_FULL_ACCESS")
    def AWS_REFACTORING_TOOLKIT_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_REFACTORING_TOOLKIT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_REFACTORING_TOOLKIT_SIDECAR_POLICY")
    def AWS_REFACTORING_TOOLKIT_SIDECAR_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_REFACTORING_TOOLKIT_SIDECAR_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_REPOST_SPACE_SUPPORT_OPERATIONS_POLICY")
    def AWS_REPOST_SPACE_SUPPORT_OPERATIONS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_REPOST_SPACE_SUPPORT_OPERATIONS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESILIENCE_HUB_ASSSESSMENT_EXECUTION_POLICY")
    def AWS_RESILIENCE_HUB_ASSSESSMENT_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESILIENCE_HUB_ASSSESSMENT_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_EXPLORER_FULL_ACCESS")
    def AWS_RESOURCE_EXPLORER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_EXPLORER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_EXPLORER_ORGANIZATIONS_ACCESS")
    def AWS_RESOURCE_EXPLORER_ORGANIZATIONS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_EXPLORER_ORGANIZATIONS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_EXPLORER_READ_ONLY_ACCESS")
    def AWS_RESOURCE_EXPLORER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_EXPLORER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS")
    def AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_FULL_ACCESS")
    def AWS_ROBO_MAKER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ROBO_MAKER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_READ_ONLY_ACCESS")
    def AWS_ROBO_MAKER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ROBO_MAKER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_SERVICE_ROLE_POLICY")
    def AWS_ROBO_MAKER_SERVICE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_ROBO_MAKER_SERVICE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SAVINGS_PLANS_FULL_ACCESS")
    def AWS_SAVINGS_PLANS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SAVINGS_PLANS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SAVINGS_PLANS_READ_ONLY_ACCESS")
    def AWS_SAVINGS_PLANS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SAVINGS_PLANS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_FULL_ACCESS")
    def AWS_SECURITY_HUB_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_HUB_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_ORGANIZATIONS_ACCESS")
    def AWS_SECURITY_HUB_ORGANIZATIONS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_HUB_ORGANIZATIONS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_READ_ONLY_ACCESS")
    def AWS_SECURITY_HUB_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_HUB_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_INCIDENT_RESPONSE_CASE_FULL_ACCESS")
    def AWS_SECURITY_INCIDENT_RESPONSE_CASE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_INCIDENT_RESPONSE_CASE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_INCIDENT_RESPONSE_FULL_ACCESS")
    def AWS_SECURITY_INCIDENT_RESPONSE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_INCIDENT_RESPONSE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_INCIDENT_RESPONSE_READ_ONLY_ACCESS")
    def AWS_SECURITY_INCIDENT_RESPONSE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SECURITY_INCIDENT_RESPONSE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS")
    def AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS")
    def AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_APP_REGISTRY_FULL_ACCESS")
    def AWS_SERVICE_CATALOG_APP_REGISTRY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_APP_REGISTRY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_APP_REGISTRY_READ_ONLY_ACCESS")
    def AWS_SERVICE_CATALOG_APP_REGISTRY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_APP_REGISTRY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS")
    def AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS")
    def AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_AUTOMATION_DIAGNOSIS_BUCKET_POLICY")
    def AWS_SSM_AUTOMATION_DIAGNOSIS_BUCKET_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_AUTOMATION_DIAGNOSIS_BUCKET_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_DIAGNOSIS_AUTOMATION_ADMINISTRATION_ROLE_POLICY")
    def AWS_SSM_DIAGNOSIS_AUTOMATION_ADMINISTRATION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_DIAGNOSIS_AUTOMATION_ADMINISTRATION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_DIAGNOSIS_AUTOMATION_EXECUTION_ROLE_POLICY")
    def AWS_SSM_DIAGNOSIS_AUTOMATION_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_DIAGNOSIS_AUTOMATION_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_DIAGNOSIS_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY")
    def AWS_SSM_DIAGNOSIS_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_DIAGNOSIS_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_REMEDIATION_AUTOMATION_ADMINISTRATION_ROLE_POLICY")
    def AWS_SSM_REMEDIATION_AUTOMATION_ADMINISTRATION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_REMEDIATION_AUTOMATION_ADMINISTRATION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_REMEDIATION_AUTOMATION_EXECUTION_ROLE_POLICY")
    def AWS_SSM_REMEDIATION_AUTOMATION_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_REMEDIATION_AUTOMATION_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSM_REMEDIATION_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY")
    def AWS_SSM_REMEDIATION_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSM_REMEDIATION_AUTOMATION_OPERATIONAL_ACCOUNT_ADMINISTRATION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_DIRECTORY_ADMINISTRATOR")
    def AWS_SSO_DIRECTORY_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSO_DIRECTORY_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_DIRECTORY_READ_ONLY")
    def AWS_SSO_DIRECTORY_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSO_DIRECTORY_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_MASTER_ACCOUNT_ADMINISTRATOR")
    def AWS_SSO_MASTER_ACCOUNT_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSO_MASTER_ACCOUNT_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_MEMBER_ACCOUNT_ADMINISTRATOR")
    def AWS_SSO_MEMBER_ACCOUNT_ADMINISTRATOR(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSO_MEMBER_ACCOUNT_ADMINISTRATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_READ_ONLY")
    def AWS_SSO_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SSO_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS")
    def AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_FULL_ACCESS")
    def AWS_STEP_FUNCTIONS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_STEP_FUNCTIONS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS")
    def AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STORAGE_GATEWAY_FULL_ACCESS")
    def AWS_STORAGE_GATEWAY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_STORAGE_GATEWAY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS")
    def AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_ACCESS")
    def AWS_SUPPORT_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SUPPORT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_APP_FULL_ACCESS")
    def AWS_SUPPORT_APP_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SUPPORT_APP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_APP_READ_ONLY_ACCESS")
    def AWS_SUPPORT_APP_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SUPPORT_APP_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_PLANS_FULL_ACCESS")
    def AWS_SUPPORT_PLANS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SUPPORT_PLANS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_PLANS_READ_ONLY_ACCESS")
    def AWS_SUPPORT_PLANS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SUPPORT_PLANS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER_ENABLE_CONFIG_RECORDING_EXECUTION_POLICY")
    def AWS_SYSTEMS_MANAGER_ENABLE_CONFIG_RECORDING_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SYSTEMS_MANAGER_ENABLE_CONFIG_RECORDING_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER_ENABLE_EXPLORER_EXECUTION_POLICY")
    def AWS_SYSTEMS_MANAGER_ENABLE_EXPLORER_EXECUTION_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SYSTEMS_MANAGER_ENABLE_EXPLORER_EXECUTION_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER_FOR_SAP_FULL_ACCESS")
    def AWS_SYSTEMS_MANAGER_FOR_SAP_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SYSTEMS_MANAGER_FOR_SAP_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER_FOR_SAP_READ_ONLY_ACCESS")
    def AWS_SYSTEMS_MANAGER_FOR_SAP_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_SYSTEMS_MANAGER_FOR_SAP_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_ASSET_SERVER_POLICY")
    def AWS_THINKBOX_ASSET_SERVER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_ASSET_SERVER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_AWS_PORTAL_ADMIN_POLICY")
    def AWS_THINKBOX_AWS_PORTAL_ADMIN_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_AWS_PORTAL_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_AWS_PORTAL_GATEWAY_POLICY")
    def AWS_THINKBOX_AWS_PORTAL_GATEWAY_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_AWS_PORTAL_GATEWAY_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_AWS_PORTAL_WORKER_POLICY")
    def AWS_THINKBOX_AWS_PORTAL_WORKER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_AWS_PORTAL_WORKER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ACCESS_POLICY")
    def AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ACCESS_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ACCESS_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ADMIN_POLICY")
    def AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ADMIN_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_DEADLINE_RESOURCE_TRACKER_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_ADMIN_POLICY")
    def AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_ADMIN_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_WORKER_POLICY")
    def AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_WORKER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_THINKBOX_DEADLINE_SPOT_EVENT_PLUGIN_WORKER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRANSFER_CONSOLE_FULL_ACCESS")
    def AWS_TRANSFER_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_TRANSFER_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRANSFER_FULL_ACCESS")
    def AWS_TRANSFER_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_TRANSFER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRANSFER_READ_ONLY_ACCESS")
    def AWS_TRANSFER_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_TRANSFER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRUSTED_ADVISOR_PRIORITY_FULL_ACCESS")
    def AWS_TRUSTED_ADVISOR_PRIORITY_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_TRUSTED_ADVISOR_PRIORITY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRUSTED_ADVISOR_PRIORITY_READ_ONLY_ACCESS")
    def AWS_TRUSTED_ADVISOR_PRIORITY_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_TRUSTED_ADVISOR_PRIORITY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_VENDOR_INSIGHTS_ASSESSOR_FULL_ACCESS")
    def AWS_VENDOR_INSIGHTS_ASSESSOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_VENDOR_INSIGHTS_ASSESSOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_VENDOR_INSIGHTS_ASSESSOR_READ_ONLY")
    def AWS_VENDOR_INSIGHTS_ASSESSOR_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_VENDOR_INSIGHTS_ASSESSOR_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_VENDOR_INSIGHTS_VENDOR_FULL_ACCESS")
    def AWS_VENDOR_INSIGHTS_VENDOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_VENDOR_INSIGHTS_VENDOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_VENDOR_INSIGHTS_VENDOR_READ_ONLY")
    def AWS_VENDOR_INSIGHTS_VENDOR_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_VENDOR_INSIGHTS_VENDOR_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_CONSOLE_FULL_ACCESS")
    def AWS_WAF_CONSOLE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_WAF_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_CONSOLE_READ_ONLY_ACCESS")
    def AWS_WAF_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_WAF_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_FULL_ACCESS")
    def AWS_WAF_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_WAF_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_READ_ONLY_ACCESS")
    def AWS_WAF_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_WAF_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WICKR_FULL_ACCESS")
    def AWS_WICKR_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_WICKR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_X_RAY_DAEMON_WRITE_ACCESS")
    def AWS_X_RAY_DAEMON_WRITE_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_X_RAY_DAEMON_WRITE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_CROSS_ACCOUNT_SHARING_CONFIGURATION")
    def AWS_XRAY_CROSS_ACCOUNT_SHARING_CONFIGURATION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_XRAY_CROSS_ACCOUNT_SHARING_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_FULL_ACCESS")
    def AWS_XRAY_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_XRAY_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_READ_ONLY_ACCESS")
    def AWS_XRAY_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_XRAY_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_WRITE_ONLY_ACCESS")
    def AWS_XRAY_WRITE_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "AWS_XRAY_WRITE_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FRONT_FULL_ACCESS")
    def CLOUD_FRONT_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_FRONT_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FRONT_READ_ONLY_ACCESS")
    def CLOUD_FRONT_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_FRONT_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_SEARCH_FULL_ACCESS")
    def CLOUD_SEARCH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_SEARCH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_SEARCH_READ_ONLY_ACCESS")
    def CLOUD_SEARCH_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_SEARCH_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_ACTIONS_EC2_ACCESS")
    def CLOUD_WATCH_ACTIONS_EC2_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_ACTIONS_EC2_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AGENT_ADMIN_POLICY")
    def CLOUD_WATCH_AGENT_ADMIN_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_AGENT_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AGENT_SERVER_POLICY")
    def CLOUD_WATCH_AGENT_SERVER_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_AGENT_SERVER_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_APPLICATION_INSIGHTS_FULL_ACCESS")
    def CLOUD_WATCH_APPLICATION_INSIGHTS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_APPLICATION_INSIGHTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_APPLICATION_INSIGHTS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_APPLICATION_INSIGHTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_APPLICATION_INSIGHTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_APPLICATION_SIGNALS_FULL_ACCESS")
    def CLOUD_WATCH_APPLICATION_SIGNALS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_APPLICATION_SIGNALS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_APPLICATION_SIGNALS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_APPLICATION_SIGNALS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_APPLICATION_SIGNALS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS")
    def CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_CROSS_ACCOUNT_SHARING_CONFIGURATION")
    def CLOUD_WATCH_CROSS_ACCOUNT_SHARING_CONFIGURATION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_CROSS_ACCOUNT_SHARING_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_FULL_ACCESS")
    def CLOUD_WATCH_EVENTS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_EVENTS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_FULL_ACCESS")
    def CLOUD_WATCH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_FULL_ACCESS_V2")
    def CLOUD_WATCH_FULL_ACCESS_V2(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_FULL_ACCESS_V2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_INTERNET_MONITOR_FULL_ACCESS")
    def CLOUD_WATCH_INTERNET_MONITOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_INTERNET_MONITOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_INTERNET_MONITOR_READ_ONLY_ACCESS")
    def CLOUD_WATCH_INTERNET_MONITOR_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_INTERNET_MONITOR_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LAMBDA_APPLICATION_SIGNALS_EXECUTION_ROLE_POLICY")
    def CLOUD_WATCH_LAMBDA_APPLICATION_SIGNALS_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_LAMBDA_APPLICATION_SIGNALS_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LAMBDA_INSIGHTS_EXECUTION_ROLE_POLICY")
    def CLOUD_WATCH_LAMBDA_INSIGHTS_EXECUTION_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_LAMBDA_INSIGHTS_EXECUTION_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LOGS_CROSS_ACCOUNT_SHARING_CONFIGURATION")
    def CLOUD_WATCH_LOGS_CROSS_ACCOUNT_SHARING_CONFIGURATION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_LOGS_CROSS_ACCOUNT_SHARING_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LOGS_FULL_ACCESS")
    def CLOUD_WATCH_LOGS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_LOGS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LOGS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_LOGS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_LOGS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_NETWORK_FLOW_MONITOR_AGENT_PUBLISH_POLICY")
    def CLOUD_WATCH_NETWORK_FLOW_MONITOR_AGENT_PUBLISH_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_NETWORK_FLOW_MONITOR_AGENT_PUBLISH_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_OPEN_SEARCH_DASHBOARD_ACCESS")
    def CLOUD_WATCH_OPEN_SEARCH_DASHBOARD_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_OPEN_SEARCH_DASHBOARD_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_OPEN_SEARCH_DASHBOARDS_FULL_ACCESS")
    def CLOUD_WATCH_OPEN_SEARCH_DASHBOARDS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_OPEN_SEARCH_DASHBOARDS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_READ_ONLY_ACCESS")
    def CLOUD_WATCH_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_SYNTHETICS_FULL_ACCESS")
    def CLOUD_WATCH_SYNTHETICS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_SYNTHETICS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_FULL_ACCESS")
    def COMPREHEND_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COMPREHEND_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_MEDICAL_FULL_ACCESS")
    def COMPREHEND_MEDICAL_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COMPREHEND_MEDICAL_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_READ_ONLY")
    def COMPREHEND_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COMPREHEND_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPUTE_OPTIMIZER_READ_ONLY_ACCESS")
    def COMPUTE_OPTIMIZER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COMPUTE_OPTIMIZER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COST_OPTIMIZATION_HUB_ADMIN_ACCESS")
    def COST_OPTIMIZATION_HUB_ADMIN_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COST_OPTIMIZATION_HUB_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COST_OPTIMIZATION_HUB_READ_ONLY_ACCESS")
    def COST_OPTIMIZATION_HUB_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "COST_OPTIMIZATION_HUB_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_FAST_LAUNCH_FULL_ACCESS")
    def EC2_FAST_LAUNCH_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "EC2_FAST_LAUNCH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_IMAGE_BUILDER_CROSS_ACCOUNT_DISTRIBUTION_ACCESS")
    def EC2_IMAGE_BUILDER_CROSS_ACCOUNT_DISTRIBUTION_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "EC2_IMAGE_BUILDER_CROSS_ACCOUNT_DISTRIBUTION_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_CONNECT")
    def EC2_INSTANCE_CONNECT(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "EC2_INSTANCE_CONNECT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER")
    def EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER_ECR_CONTAINER_BUILDS")
    def EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER_ECR_CONTAINER_BUILDS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER_ECR_CONTAINER_BUILDS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING_FULL_ACCESS")
    def ELASTIC_LOAD_BALANCING_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELASTIC_LOAD_BALANCING_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING_READ_ONLY")
    def ELASTIC_LOAD_BALANCING_READ_ONLY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELASTIC_LOAD_BALANCING_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_ACTIVATIONS_DOWNLOAD_SOFTWARE_ACCESS")
    def ELEMENTAL_ACTIVATIONS_DOWNLOAD_SOFTWARE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_ACTIVATIONS_DOWNLOAD_SOFTWARE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_ACTIVATIONS_FULL_ACCESS")
    def ELEMENTAL_ACTIVATIONS_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_ACTIVATIONS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_ACTIVATIONS_GENERATE_LICENSES")
    def ELEMENTAL_ACTIVATIONS_GENERATE_LICENSES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_ACTIVATIONS_GENERATE_LICENSES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_ACTIVATIONS_READ_ONLY_ACCESS")
    def ELEMENTAL_ACTIVATIONS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_ACTIVATIONS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS")
    def ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_APPLIANCES_SOFTWARE_READ_ONLY_ACCESS")
    def ELEMENTAL_APPLIANCES_SOFTWARE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_APPLIANCES_SOFTWARE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_SUPPORT_CENTER_FULL_ACCESS")
    def ELEMENTAL_SUPPORT_CENTER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ELEMENTAL_SUPPORT_CENTER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GAME_LIFT_CONTAINER_FLEET_POLICY")
    def GAME_LIFT_CONTAINER_FLEET_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GAME_LIFT_CONTAINER_FLEET_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GAME_LIFT_GAME_SERVER_GROUP_POLICY")
    def GAME_LIFT_GAME_SERVER_GROUP_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GAME_LIFT_GAME_SERVER_GROUP_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_FULL_ACCESS")
    def GLOBAL_ACCELERATOR_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GLOBAL_ACCELERATOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_READ_ONLY_ACCESS")
    def GLOBAL_ACCELERATOR_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GLOBAL_ACCELERATOR_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GROUND_TRUTH_SYNTHETIC_CONSOLE_FULL_ACCESS")
    def GROUND_TRUTH_SYNTHETIC_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GROUND_TRUTH_SYNTHETIC_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GROUND_TRUTH_SYNTHETIC_CONSOLE_READ_ONLY_ACCESS")
    def GROUND_TRUTH_SYNTHETIC_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "GROUND_TRUTH_SYNTHETIC_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ADVISOR_READ_ONLY")
    def IAM_ACCESS_ADVISOR_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_ACCESS_ADVISOR_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ANALYZER_FULL_ACCESS")
    def IAM_ACCESS_ANALYZER_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_ACCESS_ANALYZER_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS")
    def IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_FULL_ACCESS")
    def IAM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_READ_ONLY_ACCESS")
    def IAM_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS")
    def IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_CHANGE_PASSWORD")
    def IAM_USER_CHANGE_PASSWORD(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_USER_CHANGE_PASSWORD"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_SSH_KEYS")
    def IAM_USER_SSH_KEYS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IAM_USER_SSH_KEYS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IVS_FULL_ACCESS")
    def IVS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IVS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IVS_READ_ONLY_ACCESS")
    def IVS_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "IVS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MEDIA_CONNECT_GATEWAY_INSTANCE_ROLE_POLICY")
    def MEDIA_CONNECT_GATEWAY_INSTANCE_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "MEDIA_CONNECT_GATEWAY_INSTANCE_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_CONSOLE_FULL_ACCESS")
    def NEPTUNE_CONSOLE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "NEPTUNE_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_FULL_ACCESS")
    def NEPTUNE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "NEPTUNE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_GRAPH_READ_ONLY_ACCESS")
    def NEPTUNE_GRAPH_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "NEPTUNE_GRAPH_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_READ_ONLY_ACCESS")
    def NEPTUNE_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "NEPTUNE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OAM_FULL_ACCESS")
    def OAM_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "OAM_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OAM_READ_ONLY_ACCESS")
    def OAM_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "OAM_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PARTNER_CENTRAL_ACCOUNT_MANAGEMENT_USER_ROLE_ASSOCIATION")
    def PARTNER_CENTRAL_ACCOUNT_MANAGEMENT_USER_ROLE_ASSOCIATION(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "PARTNER_CENTRAL_ACCOUNT_MANAGEMENT_USER_ROLE_ASSOCIATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POWER_USER_ACCESS")
    def POWER_USER_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "POWER_USER_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="Q_BUSINESS_QUICKSIGHT_PLUGIN_POLICY")
    def Q_BUSINESS_QUICKSIGHT_PLUGIN_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "Q_BUSINESS_QUICKSIGHT_PLUGIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="READ_ONLY_ACCESS")
    def READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_GROUPS_AND_TAG_EDITOR_FULL_ACCESS")
    def RESOURCE_GROUPS_AND_TAG_EDITOR_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "RESOURCE_GROUPS_AND_TAG_EDITOR_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_GROUPS_AND_TAG_EDITOR_READ_ONLY_ACCESS")
    def RESOURCE_GROUPS_AND_TAG_EDITOR_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "RESOURCE_GROUPS_AND_TAG_EDITOR_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_GROUPS_TAGGING_API_TAG_UNTAG_SUPPORTED_RESOURCES")
    def RESOURCE_GROUPS_TAGGING_API_TAG_UNTAG_SUPPORTED_RESOURCES(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "RESOURCE_GROUPS_TAGGING_API_TAG_UNTAG_SUPPORTED_RESOURCES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROSA_MANAGE_SUBSCRIPTION")
    def ROSA_MANAGE_SUBSCRIPTION(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "ROSA_MANAGE_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGE_MAKER_STUDIO_FULL_ACCESS")
    def SAGE_MAKER_STUDIO_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SAGE_MAKER_STUDIO_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGE_MAKER_STUDIO_PROJECT_ROLE_MACHINE_LEARNING_POLICY")
    def SAGE_MAKER_STUDIO_PROJECT_ROLE_MACHINE_LEARNING_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SAGE_MAKER_STUDIO_PROJECT_ROLE_MACHINE_LEARNING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_PERMISSIONS_BOUNDARY")
    def SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_PERMISSIONS_BOUNDARY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_PERMISSIONS_BOUNDARY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_POLICY")
    def SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_POLICY(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SAGE_MAKER_STUDIO_PROJECT_USER_ROLE_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER_READ_WRITE")
    def SECRETS_MANAGER_READ_WRITE(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SECRETS_MANAGER_READ_WRITE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECURITY_AUDIT")
    def SECURITY_AUDIT(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SECURITY_AUDIT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVER_MIGRATION_CONNECTOR")
    def SERVER_MIGRATION_CONNECTOR(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SERVER_MIGRATION_CONNECTOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVER_MIGRATION_SERVICE_CONSOLE_FULL_ACCESS")
    def SERVER_MIGRATION_SERVICE_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SERVER_MIGRATION_SERVICE_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS_FULL_ACCESS")
    def SERVICE_QUOTAS_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SERVICE_QUOTAS_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS_READ_ONLY_ACCESS")
    def SERVICE_QUOTAS_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SERVICE_QUOTAS_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SIMPLE_WORKFLOW_FULL_ACCESS")
    def SIMPLE_WORKFLOW_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "SIMPLE_WORKFLOW_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRANSLATE_FULL_ACCESS")
    def TRANSLATE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "TRANSLATE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRANSLATE_READ_ONLY")
    def TRANSLATE_READ_ONLY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "TRANSLATE_READ_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_LATTICE_FULL_ACCESS")
    def VPC_LATTICE_FULL_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "VPC_LATTICE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_LATTICE_READ_ONLY_ACCESS")
    def VPC_LATTICE_READ_ONLY_ACCESS(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "VPC_LATTICE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_LATTICE_SERVICES_INVOKE_ACCESS")
    def VPC_LATTICE_SERVICES_INVOKE_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "VPC_LATTICE_SERVICES_INVOKE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WELL_ARCHITECTED_CONSOLE_FULL_ACCESS")
    def WELL_ARCHITECTED_CONSOLE_FULL_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "WELL_ARCHITECTED_CONSOLE_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS")
    def WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS(
        cls,
    ) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORK_LINK_SERVICE_ROLE_POLICY")
    def WORK_LINK_SERVICE_ROLE_POLICY(cls) -> _aws_cdk_aws_iam_ceddda9d.IManagedPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IManagedPolicy, jsii.sget(cls, "WORK_LINK_SERVICE_ROLE_POLICY"))


@jsii.data_type(
    jsii_type="@cdklabs/cdk-proserve-lib.types.LambdaConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "log_group_retention": "logGroupRetention",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "security_groups": "securityGroups",
        "subnets": "subnets",
        "vpc": "vpc",
    },
)
class LambdaConfiguration:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
        log_group_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param dead_letter_queue: (experimental) Optional SQS queue to use as a dead letter queue.
        :param log_group_retention: (experimental) Optional retention period for the Lambda functions log group. Default: RetentionDays.ONE_MONTH
        :param reserved_concurrent_executions: (experimental) The number of concurrent executions for the provider Lambda function. Default: 5
        :param security_groups: (experimental) Security groups to attach to the provider Lambda functions.
        :param subnets: (experimental) Optional subnet selection for the Lambda functions.
        :param vpc: (experimental) VPC where the Lambda functions will be deployed.

        :stability: experimental
        '''
        if isinstance(subnets, dict):
            subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e572f0d30fd79ee590fe9464ce9e2e98acbf2c78d2f4d37c841c325412590fd9)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument log_group_retention", value=log_group_retention, expected_type=type_hints["log_group_retention"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if log_group_retention is not None:
            self._values["log_group_retention"] = log_group_retention
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnets is not None:
            self._values["subnets"] = subnets
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue]:
        '''(experimental) Optional SQS queue to use as a dead letter queue.

        :stability: experimental
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue], result)

    @builtins.property
    def log_group_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''(experimental) Optional retention period for the Lambda functions log group.

        :default: RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_group_retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of concurrent executions for the provider Lambda function.

        Default: 5

        :stability: experimental
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]]:
        '''(experimental) Security groups to attach to the provider Lambda functions.

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]], result)

    @builtins.property
    def subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''(experimental) Optional subnet selection for the Lambda functions.

        :stability: experimental
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''(experimental) VPC where the Lambda functions will be deployed.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsCustomResourceLambdaConfiguration",
    "AwsManagedPolicy",
    "LambdaConfiguration",
]

publication.publish()

def _typecheckingstub__94c5cee93e244643d0253938483ebf4729a03d1dbc4432b65477c09475f2f439(
    *,
    subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e572f0d30fd79ee590fe9464ce9e2e98acbf2c78d2f4d37c841c325412590fd9(
    *,
    dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
    log_group_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass
