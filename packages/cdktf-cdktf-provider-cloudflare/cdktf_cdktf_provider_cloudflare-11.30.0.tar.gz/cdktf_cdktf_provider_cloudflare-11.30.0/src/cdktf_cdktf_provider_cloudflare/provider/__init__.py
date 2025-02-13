r'''
# `provider`

Refer to the Terraform Registry for docs: [`cloudflare`](https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs).
'''
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

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class CloudflareProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.provider.CloudflareProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs cloudflare}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_base_path: typing.Optional[builtins.str] = None,
        api_client_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        api_hostname: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        api_user_service_key: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        max_backoff: typing.Optional[jsii.Number] = None,
        min_backoff: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        rps: typing.Optional[jsii.Number] = None,
        user_agent_operator_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs cloudflare} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#alias CloudflareProvider#alias}
        :param api_base_path: Configure the base path used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_BASE_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_base_path CloudflareProvider#api_base_path}
        :param api_client_logging: Whether to print logs from the API client (using the default log library logger). Alternatively, can be configured using the ``CLOUDFLARE_API_CLIENT_LOGGING`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_client_logging CloudflareProvider#api_client_logging}
        :param api_hostname: Configure the hostname used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_HOSTNAME`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_hostname CloudflareProvider#api_hostname}
        :param api_key: The API key for operations. Alternatively, can be configured using the ``CLOUDFLARE_API_KEY`` environment variable. API keys are `now considered legacy by Cloudflare <https://developers.cloudflare.com/fundamentals/api/get-started/keys/#limitations>`_, API tokens should be used instead. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_key CloudflareProvider#api_key}
        :param api_token: The API Token for operations. Alternatively, can be configured using the ``CLOUDFLARE_API_TOKEN`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_token CloudflareProvider#api_token}
        :param api_user_service_key: A special Cloudflare API key good for a restricted set of endpoints. Alternatively, can be configured using the ``CLOUDFLARE_API_USER_SERVICE_KEY`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_user_service_key CloudflareProvider#api_user_service_key}
        :param email: A registered Cloudflare email address. Alternatively, can be configured using the ``CLOUDFLARE_EMAIL`` environment variable. Required when using ``api_key``. Conflicts with ``api_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#email CloudflareProvider#email}
        :param max_backoff: Maximum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MAX_BACKOFF`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#max_backoff CloudflareProvider#max_backoff}
        :param min_backoff: Minimum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MIN_BACKOFF`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#min_backoff CloudflareProvider#min_backoff}
        :param retries: Maximum number of retries to perform when an API request fails. Alternatively, can be configured using the ``CLOUDFLARE_RETRIES`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#retries CloudflareProvider#retries}
        :param rps: RPS limit to apply when making calls to the API. Alternatively, can be configured using the ``CLOUDFLARE_RPS`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#rps CloudflareProvider#rps}
        :param user_agent_operator_suffix: A value to append to the HTTP User Agent for all API calls. This value is not something most users need to modify however, if you are using a non-standard provider or operator configuration, this is recommended to assist in uniquely identifying your traffic. **Setting this value will remove the Terraform version from the HTTP User Agent string and may have unintended consequences**. Alternatively, can be configured using the ``CLOUDFLARE_USER_AGENT_OPERATOR_SUFFIX`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#user_agent_operator_suffix CloudflareProvider#user_agent_operator_suffix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c8ed5006d3e3fa5a2c23fad8b013482f81a5f8eb784f19b3759f2301dfe852)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CloudflareProviderConfig(
            alias=alias,
            api_base_path=api_base_path,
            api_client_logging=api_client_logging,
            api_hostname=api_hostname,
            api_key=api_key,
            api_token=api_token,
            api_user_service_key=api_user_service_key,
            email=email,
            max_backoff=max_backoff,
            min_backoff=min_backoff,
            retries=retries,
            rps=rps,
            user_agent_operator_suffix=user_agent_operator_suffix,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a CloudflareProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CloudflareProvider to import.
        :param import_from_id: The id of the existing CloudflareProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CloudflareProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3d75b6652fb7c29104bc3370eada3fb496826950c55f9632e9bb68cf445f9c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiBasePath")
    def reset_api_base_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiBasePath", []))

    @jsii.member(jsii_name="resetApiClientLogging")
    def reset_api_client_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiClientLogging", []))

    @jsii.member(jsii_name="resetApiHostname")
    def reset_api_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiHostname", []))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetApiToken")
    def reset_api_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiToken", []))

    @jsii.member(jsii_name="resetApiUserServiceKey")
    def reset_api_user_service_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUserServiceKey", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetMaxBackoff")
    def reset_max_backoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBackoff", []))

    @jsii.member(jsii_name="resetMinBackoff")
    def reset_min_backoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinBackoff", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetRps")
    def reset_rps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRps", []))

    @jsii.member(jsii_name="resetUserAgentOperatorSuffix")
    def reset_user_agent_operator_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgentOperatorSuffix", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiBasePathInput")
    def api_base_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiBasePathInput"))

    @builtins.property
    @jsii.member(jsii_name="apiClientLoggingInput")
    def api_client_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "apiClientLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="apiHostnameInput")
    def api_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUserServiceKeyInput")
    def api_user_service_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUserServiceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBackoffInput")
    def max_backoff_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBackoffInput"))

    @builtins.property
    @jsii.member(jsii_name="minBackoffInput")
    def min_backoff_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minBackoffInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="rpsInput")
    def rps_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rpsInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentOperatorSuffixInput")
    def user_agent_operator_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgentOperatorSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c930854d6ea7147c8ed15c32af3e48deafd93fb8f753d8178b8b2404d9b1316)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiBasePath")
    def api_base_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiBasePath"))

    @api_base_path.setter
    def api_base_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd6f8b7f368a3cc06477023b681233eab19cbaf510b5e85702393202ec0cd20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiBasePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiClientLogging")
    def api_client_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "apiClientLogging"))

    @api_client_logging.setter
    def api_client_logging(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__362ee90293451c3696775fb7de5a8e093f38927b65a4c5f9ca942e4d035c8da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiClientLogging", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiHostname")
    def api_hostname(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiHostname"))

    @api_hostname.setter
    def api_hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__230943f59a472be1d2d28ee0bb3240b282a322cc04bbeb8960ec44239b14f5e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiHostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dcacca017c51d23cee3b3d542660b1a4889ec7e22f721fbccb9c95ae9aa0db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64356e8c2024559d318fd9a82d7a6699d2313b75587320a5a36f4dbc9d3854ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="apiUserServiceKey")
    def api_user_service_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUserServiceKey"))

    @api_user_service_key.setter
    def api_user_service_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d647dffa5e61b66c498aa264eb4a7f4a10e26bd61db9ae56567d4ad0ba322f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUserServiceKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d25273a46ef4056e832d8bd4e26168c3442fb9b316190a8404e6a4d5efdd33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxBackoff")
    def max_backoff(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBackoff"))

    @max_backoff.setter
    def max_backoff(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da979d78df94371166a65477f08b00c7d8de621e9f19b053808260275c75a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBackoff", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minBackoff")
    def min_backoff(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minBackoff"))

    @min_backoff.setter
    def min_backoff(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d54bf3da23fb906ce1f20aef0e7fadbeb7e472769389d9467b4984a5f424a082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minBackoff", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0423aae6016c423d5fcd693bbcb499b7732e69018647dffedbcde262b0ec05a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rps")
    def rps(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rps"))

    @rps.setter
    def rps(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddae0e7641f02ffd3db00698a36bd78485fedee1930d8e804c45c1c2f11855d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rps", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userAgentOperatorSuffix")
    def user_agent_operator_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgentOperatorSuffix"))

    @user_agent_operator_suffix.setter
    def user_agent_operator_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03dbeb5898bad7db445f44a34b30a3ddbe87bdf6addeb6a73105fcfefbcb8f2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAgentOperatorSuffix", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.provider.CloudflareProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "api_base_path": "apiBasePath",
        "api_client_logging": "apiClientLogging",
        "api_hostname": "apiHostname",
        "api_key": "apiKey",
        "api_token": "apiToken",
        "api_user_service_key": "apiUserServiceKey",
        "email": "email",
        "max_backoff": "maxBackoff",
        "min_backoff": "minBackoff",
        "retries": "retries",
        "rps": "rps",
        "user_agent_operator_suffix": "userAgentOperatorSuffix",
    },
)
class CloudflareProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_base_path: typing.Optional[builtins.str] = None,
        api_client_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        api_hostname: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        api_user_service_key: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        max_backoff: typing.Optional[jsii.Number] = None,
        min_backoff: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        rps: typing.Optional[jsii.Number] = None,
        user_agent_operator_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#alias CloudflareProvider#alias}
        :param api_base_path: Configure the base path used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_BASE_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_base_path CloudflareProvider#api_base_path}
        :param api_client_logging: Whether to print logs from the API client (using the default log library logger). Alternatively, can be configured using the ``CLOUDFLARE_API_CLIENT_LOGGING`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_client_logging CloudflareProvider#api_client_logging}
        :param api_hostname: Configure the hostname used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_HOSTNAME`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_hostname CloudflareProvider#api_hostname}
        :param api_key: The API key for operations. Alternatively, can be configured using the ``CLOUDFLARE_API_KEY`` environment variable. API keys are `now considered legacy by Cloudflare <https://developers.cloudflare.com/fundamentals/api/get-started/keys/#limitations>`_, API tokens should be used instead. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_key CloudflareProvider#api_key}
        :param api_token: The API Token for operations. Alternatively, can be configured using the ``CLOUDFLARE_API_TOKEN`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_token CloudflareProvider#api_token}
        :param api_user_service_key: A special Cloudflare API key good for a restricted set of endpoints. Alternatively, can be configured using the ``CLOUDFLARE_API_USER_SERVICE_KEY`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_user_service_key CloudflareProvider#api_user_service_key}
        :param email: A registered Cloudflare email address. Alternatively, can be configured using the ``CLOUDFLARE_EMAIL`` environment variable. Required when using ``api_key``. Conflicts with ``api_token``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#email CloudflareProvider#email}
        :param max_backoff: Maximum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MAX_BACKOFF`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#max_backoff CloudflareProvider#max_backoff}
        :param min_backoff: Minimum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MIN_BACKOFF`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#min_backoff CloudflareProvider#min_backoff}
        :param retries: Maximum number of retries to perform when an API request fails. Alternatively, can be configured using the ``CLOUDFLARE_RETRIES`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#retries CloudflareProvider#retries}
        :param rps: RPS limit to apply when making calls to the API. Alternatively, can be configured using the ``CLOUDFLARE_RPS`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#rps CloudflareProvider#rps}
        :param user_agent_operator_suffix: A value to append to the HTTP User Agent for all API calls. This value is not something most users need to modify however, if you are using a non-standard provider or operator configuration, this is recommended to assist in uniquely identifying your traffic. **Setting this value will remove the Terraform version from the HTTP User Agent string and may have unintended consequences**. Alternatively, can be configured using the ``CLOUDFLARE_USER_AGENT_OPERATOR_SUFFIX`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#user_agent_operator_suffix CloudflareProvider#user_agent_operator_suffix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be8b5a991fa153b7d55c84e6205ae7cb1dbfa2bb0998c1fc9f399200956addc4)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_base_path", value=api_base_path, expected_type=type_hints["api_base_path"])
            check_type(argname="argument api_client_logging", value=api_client_logging, expected_type=type_hints["api_client_logging"])
            check_type(argname="argument api_hostname", value=api_hostname, expected_type=type_hints["api_hostname"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument api_user_service_key", value=api_user_service_key, expected_type=type_hints["api_user_service_key"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument max_backoff", value=max_backoff, expected_type=type_hints["max_backoff"])
            check_type(argname="argument min_backoff", value=min_backoff, expected_type=type_hints["min_backoff"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument rps", value=rps, expected_type=type_hints["rps"])
            check_type(argname="argument user_agent_operator_suffix", value=user_agent_operator_suffix, expected_type=type_hints["user_agent_operator_suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_base_path is not None:
            self._values["api_base_path"] = api_base_path
        if api_client_logging is not None:
            self._values["api_client_logging"] = api_client_logging
        if api_hostname is not None:
            self._values["api_hostname"] = api_hostname
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_token is not None:
            self._values["api_token"] = api_token
        if api_user_service_key is not None:
            self._values["api_user_service_key"] = api_user_service_key
        if email is not None:
            self._values["email"] = email
        if max_backoff is not None:
            self._values["max_backoff"] = max_backoff
        if min_backoff is not None:
            self._values["min_backoff"] = min_backoff
        if retries is not None:
            self._values["retries"] = retries
        if rps is not None:
            self._values["rps"] = rps
        if user_agent_operator_suffix is not None:
            self._values["user_agent_operator_suffix"] = user_agent_operator_suffix

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#alias CloudflareProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_base_path(self) -> typing.Optional[builtins.str]:
        '''Configure the base path used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_BASE_PATH`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_base_path CloudflareProvider#api_base_path}
        '''
        result = self._values.get("api_base_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_client_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to print logs from the API client (using the default log library logger).

        Alternatively, can be configured using the ``CLOUDFLARE_API_CLIENT_LOGGING`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_client_logging CloudflareProvider#api_client_logging}
        '''
        result = self._values.get("api_client_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def api_hostname(self) -> typing.Optional[builtins.str]:
        '''Configure the hostname used by the API client. Alternatively, can be configured using the ``CLOUDFLARE_API_HOSTNAME`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_hostname CloudflareProvider#api_hostname}
        '''
        result = self._values.get("api_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''The API key for operations.

        Alternatively, can be configured using the ``CLOUDFLARE_API_KEY`` environment variable. API keys are `now considered legacy by Cloudflare <https://developers.cloudflare.com/fundamentals/api/get-started/keys/#limitations>`_, API tokens should be used instead. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_key CloudflareProvider#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_token(self) -> typing.Optional[builtins.str]:
        '''The API Token for operations.

        Alternatively, can be configured using the ``CLOUDFLARE_API_TOKEN`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_token CloudflareProvider#api_token}
        '''
        result = self._values.get("api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_user_service_key(self) -> typing.Optional[builtins.str]:
        '''A special Cloudflare API key good for a restricted set of endpoints.

        Alternatively, can be configured using the ``CLOUDFLARE_API_USER_SERVICE_KEY`` environment variable. Must provide only one of ``api_key``, ``api_token``, ``api_user_service_key``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#api_user_service_key CloudflareProvider#api_user_service_key}
        '''
        result = self._values.get("api_user_service_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''A registered Cloudflare email address.

        Alternatively, can be configured using the ``CLOUDFLARE_EMAIL`` environment variable. Required when using ``api_key``. Conflicts with ``api_token``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#email CloudflareProvider#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_backoff(self) -> typing.Optional[jsii.Number]:
        '''Maximum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MAX_BACKOFF`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#max_backoff CloudflareProvider#max_backoff}
        '''
        result = self._values.get("max_backoff")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_backoff(self) -> typing.Optional[jsii.Number]:
        '''Minimum backoff period in seconds after failed API calls. Alternatively, can be configured using the ``CLOUDFLARE_MIN_BACKOFF`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#min_backoff CloudflareProvider#min_backoff}
        '''
        result = self._values.get("min_backoff")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of retries to perform when an API request fails.

        Alternatively, can be configured using the ``CLOUDFLARE_RETRIES`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#retries CloudflareProvider#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rps(self) -> typing.Optional[jsii.Number]:
        '''RPS limit to apply when making calls to the API. Alternatively, can be configured using the ``CLOUDFLARE_RPS`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#rps CloudflareProvider#rps}
        '''
        result = self._values.get("rps")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_agent_operator_suffix(self) -> typing.Optional[builtins.str]:
        '''A value to append to the HTTP User Agent for all API calls.

        This value is not something most users need to modify however, if you are using a non-standard provider or operator configuration, this is recommended to assist in uniquely identifying your traffic. **Setting this value will remove the Terraform version from the HTTP User Agent string and may have unintended consequences**. Alternatively, can be configured using the ``CLOUDFLARE_USER_AGENT_OPERATOR_SUFFIX`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs#user_agent_operator_suffix CloudflareProvider#user_agent_operator_suffix}
        '''
        result = self._values.get("user_agent_operator_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudflareProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudflareProvider",
    "CloudflareProviderConfig",
]

publication.publish()

def _typecheckingstub__e6c8ed5006d3e3fa5a2c23fad8b013482f81a5f8eb784f19b3759f2301dfe852(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    api_base_path: typing.Optional[builtins.str] = None,
    api_client_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    api_hostname: typing.Optional[builtins.str] = None,
    api_key: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    api_user_service_key: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    max_backoff: typing.Optional[jsii.Number] = None,
    min_backoff: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    rps: typing.Optional[jsii.Number] = None,
    user_agent_operator_suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3d75b6652fb7c29104bc3370eada3fb496826950c55f9632e9bb68cf445f9c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c930854d6ea7147c8ed15c32af3e48deafd93fb8f753d8178b8b2404d9b1316(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd6f8b7f368a3cc06477023b681233eab19cbaf510b5e85702393202ec0cd20(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__362ee90293451c3696775fb7de5a8e093f38927b65a4c5f9ca942e4d035c8da9(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__230943f59a472be1d2d28ee0bb3240b282a322cc04bbeb8960ec44239b14f5e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcacca017c51d23cee3b3d542660b1a4889ec7e22f721fbccb9c95ae9aa0db5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64356e8c2024559d318fd9a82d7a6699d2313b75587320a5a36f4dbc9d3854ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d647dffa5e61b66c498aa264eb4a7f4a10e26bd61db9ae56567d4ad0ba322f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d25273a46ef4056e832d8bd4e26168c3442fb9b316190a8404e6a4d5efdd33(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da979d78df94371166a65477f08b00c7d8de621e9f19b053808260275c75a8b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54bf3da23fb906ce1f20aef0e7fadbeb7e472769389d9467b4984a5f424a082(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0423aae6016c423d5fcd693bbcb499b7732e69018647dffedbcde262b0ec05a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddae0e7641f02ffd3db00698a36bd78485fedee1930d8e804c45c1c2f11855d0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03dbeb5898bad7db445f44a34b30a3ddbe87bdf6addeb6a73105fcfefbcb8f2e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8b5a991fa153b7d55c84e6205ae7cb1dbfa2bb0998c1fc9f399200956addc4(
    *,
    alias: typing.Optional[builtins.str] = None,
    api_base_path: typing.Optional[builtins.str] = None,
    api_client_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    api_hostname: typing.Optional[builtins.str] = None,
    api_key: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    api_user_service_key: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    max_backoff: typing.Optional[jsii.Number] = None,
    min_backoff: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    rps: typing.Optional[jsii.Number] = None,
    user_agent_operator_suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
