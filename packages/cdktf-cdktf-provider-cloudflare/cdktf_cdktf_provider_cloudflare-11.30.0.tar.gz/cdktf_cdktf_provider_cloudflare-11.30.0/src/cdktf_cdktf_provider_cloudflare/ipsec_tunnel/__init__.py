r'''
# `cloudflare_ipsec_tunnel`

Refer to the Terraform Registry for docs: [`cloudflare_ipsec_tunnel`](https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel).
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


class IpsecTunnel(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ipsecTunnel.IpsecTunnel",
):
    '''Represents a {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel cloudflare_ipsec_tunnel}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cloudflare_endpoint: builtins.str,
        customer_endpoint: builtins.str,
        interface_address: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allow_null_cipher: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        fqdn_id: typing.Optional[builtins.str] = None,
        health_check_direction: typing.Optional[builtins.str] = None,
        health_check_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check_rate: typing.Optional[builtins.str] = None,
        health_check_target: typing.Optional[builtins.str] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        hex_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        psk: typing.Optional[builtins.str] = None,
        remote_id: typing.Optional[builtins.str] = None,
        replay_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel cloudflare_ipsec_tunnel} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cloudflare_endpoint: IP address assigned to the Cloudflare side of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#cloudflare_endpoint IpsecTunnel#cloudflare_endpoint}
        :param customer_endpoint: IP address assigned to the customer side of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#customer_endpoint IpsecTunnel#customer_endpoint}
        :param interface_address: 31-bit prefix (/31 in CIDR notation) supporting 2 hosts, one for each side of the tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#interface_address IpsecTunnel#interface_address}
        :param name: Name of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#name IpsecTunnel#name}
        :param account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#account_id IpsecTunnel#account_id}
        :param allow_null_cipher: Specifies if this tunnel may use a null cipher (ENCR_NULL) in Phase 2. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#allow_null_cipher IpsecTunnel#allow_null_cipher}
        :param description: An optional description of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#description IpsecTunnel#description}
        :param fqdn_id: ``remote_id`` in the form of a fqdn. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#fqdn_id IpsecTunnel#fqdn_id}
        :param health_check_direction: Specifies the direction for the health check. Available values: ``unidirectional``, ``bidirectional`` Default: ``unidirectional``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_direction IpsecTunnel#health_check_direction}
        :param health_check_enabled: Specifies if ICMP tunnel health checks are enabled. Default: ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_enabled IpsecTunnel#health_check_enabled}
        :param health_check_rate: Specifies the ICMP rate for the health check. Available values: ``low``, ``mid``, ``high`` Default: ``mid``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_rate IpsecTunnel#health_check_rate}
        :param health_check_target: The IP address of the customer endpoint that will receive tunnel health checks. Default: ``<customer_gre_endpoint>``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_target IpsecTunnel#health_check_target}
        :param health_check_type: Specifies the ICMP echo type for the health check (``request`` or ``reply``). Available values: ``request``, ``reply`` Default: ``reply``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_type IpsecTunnel#health_check_type}
        :param hex_id: ``remote_id`` as a hex string. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#hex_id IpsecTunnel#hex_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#id IpsecTunnel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param psk: Pre shared key to be used with the IPsec tunnel. If left unset, it will be autogenerated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#psk IpsecTunnel#psk}
        :param remote_id: ID to be used while setting up the IPsec tunnel. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#remote_id IpsecTunnel#remote_id}
        :param replay_protection: Specifies if replay protection is enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#replay_protection IpsecTunnel#replay_protection}
        :param user_id: ``remote_id`` in the form of an email address. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#user_id IpsecTunnel#user_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca1b3e56ac7517da72e0f79208ea920dfeab531292da51ba1b9163a57d83f04b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IpsecTunnelConfig(
            cloudflare_endpoint=cloudflare_endpoint,
            customer_endpoint=customer_endpoint,
            interface_address=interface_address,
            name=name,
            account_id=account_id,
            allow_null_cipher=allow_null_cipher,
            description=description,
            fqdn_id=fqdn_id,
            health_check_direction=health_check_direction,
            health_check_enabled=health_check_enabled,
            health_check_rate=health_check_rate,
            health_check_target=health_check_target,
            health_check_type=health_check_type,
            hex_id=hex_id,
            id=id,
            psk=psk,
            remote_id=remote_id,
            replay_protection=replay_protection,
            user_id=user_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a IpsecTunnel resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the IpsecTunnel to import.
        :param import_from_id: The id of the existing IpsecTunnel that should be imported. Refer to the {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the IpsecTunnel to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db04a4ed789ae861c04f83f86486e54c31b08abba6fb82bdd1a7d350428906f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAllowNullCipher")
    def reset_allow_null_cipher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowNullCipher", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFqdnId")
    def reset_fqdn_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFqdnId", []))

    @jsii.member(jsii_name="resetHealthCheckDirection")
    def reset_health_check_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckDirection", []))

    @jsii.member(jsii_name="resetHealthCheckEnabled")
    def reset_health_check_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckEnabled", []))

    @jsii.member(jsii_name="resetHealthCheckRate")
    def reset_health_check_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckRate", []))

    @jsii.member(jsii_name="resetHealthCheckTarget")
    def reset_health_check_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckTarget", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @jsii.member(jsii_name="resetHexId")
    def reset_hex_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHexId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPsk")
    def reset_psk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPsk", []))

    @jsii.member(jsii_name="resetRemoteId")
    def reset_remote_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteId", []))

    @jsii.member(jsii_name="resetReplayProtection")
    def reset_replay_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplayProtection", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

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
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowNullCipherInput")
    def allow_null_cipher_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowNullCipherInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudflareEndpointInput")
    def cloudflare_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudflareEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="customerEndpointInput")
    def customer_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fqdnIdInput")
    def fqdn_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fqdnIdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckDirectionInput")
    def health_check_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckEnabledInput")
    def health_check_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "healthCheckEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckRateInput")
    def health_check_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckRateInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTargetInput")
    def health_check_target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="hexIdInput")
    def hex_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hexIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceAddressInput")
    def interface_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pskInput")
    def psk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pskInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIdInput")
    def remote_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replayProtectionInput")
    def replay_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "replayProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de5a37c8e08d3e8ba523b5eb03edb5e7a63c70b4fd7d05cc6492540d46d410b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowNullCipher")
    def allow_null_cipher(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowNullCipher"))

    @allow_null_cipher.setter
    def allow_null_cipher(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564bca3f42872d1f7bf6d5e39da0381b272d0a5e857825b4f51b2b601f712784)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowNullCipher", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cloudflareEndpoint")
    def cloudflare_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudflareEndpoint"))

    @cloudflare_endpoint.setter
    def cloudflare_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a258b37536c627d455f9bfb82e0a91c26e8083bf1b07af8378c56b337e678d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudflareEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customerEndpoint")
    def customer_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerEndpoint"))

    @customer_endpoint.setter
    def customer_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05589e72a25bbd3766b87351b6a73a02ecde5ab814310b1adfc71cfcf595067e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23ff8040934f4a14ad16b7c564a8c0285a80d3fbe6af4700dba33fdca2f2b33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fqdnId")
    def fqdn_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdnId"))

    @fqdn_id.setter
    def fqdn_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc92d0a8f7c3c519926ec4ed2a5ffc1022239a5e20e2e4340dbcbfd900621841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fqdnId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckDirection")
    def health_check_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckDirection"))

    @health_check_direction.setter
    def health_check_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be673b3e457d3e5067d9cc24acebf397b9c7779b542df116054cc0b0a14b370f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckDirection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckEnabled")
    def health_check_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "healthCheckEnabled"))

    @health_check_enabled.setter
    def health_check_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2067562cd61574a0df9ad18d40bb4153cfde0e42cbfddba1909cb25d4938501)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckRate")
    def health_check_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckRate"))

    @health_check_rate.setter
    def health_check_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21be19939a649483c7f1ce2c73145e22a95c49bc94232aa360483819789d40f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckRate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckTarget")
    def health_check_target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckTarget"))

    @health_check_target.setter
    def health_check_target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7178761a8e0b71f26a69a26d9cb659912a6afe04dde576b74dfbcbf3b0394ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckTarget", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa01f96f8e91193acf6863e1d1871cb8bcd4d5e04df22df98046b006bae00cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hexId")
    def hex_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hexId"))

    @hex_id.setter
    def hex_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2ebd25b383116af614d36b5718f6d879d08b8fc0affa2b358f1281e67b00c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hexId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a76430fbd52017016629f079e11f1901b6b056d7d14744a8939793611281bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="interfaceAddress")
    def interface_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interfaceAddress"))

    @interface_address.setter
    def interface_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a84dfd6e30da71066ca70f0fc952e648a29c34e00f32ed2a6a58d96b3af9143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interfaceAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42316ada419534ad06a5a9fab08d9c56cfb79d39c0ab826d24883cd4fa3118e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="psk")
    def psk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "psk"))

    @psk.setter
    def psk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4a017df6ced225deb5bdcf508c1af69d0f0145a222e78c09514d93dfc7bde7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "psk", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteId")
    def remote_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteId"))

    @remote_id.setter
    def remote_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4bfd59910cd640d8b0621b0b1882cbc14b35f2b6449fe324858eee8826207f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="replayProtection")
    def replay_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "replayProtection"))

    @replay_protection.setter
    def replay_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8382a52091835929299e67a6928cfbe1c617335d4344f4d88398188d79c0160c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replayProtection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf4c962c56c6b0db71de36c986f2c434ea050f87b637efbbce8fe81f69345b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ipsecTunnel.IpsecTunnelConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cloudflare_endpoint": "cloudflareEndpoint",
        "customer_endpoint": "customerEndpoint",
        "interface_address": "interfaceAddress",
        "name": "name",
        "account_id": "accountId",
        "allow_null_cipher": "allowNullCipher",
        "description": "description",
        "fqdn_id": "fqdnId",
        "health_check_direction": "healthCheckDirection",
        "health_check_enabled": "healthCheckEnabled",
        "health_check_rate": "healthCheckRate",
        "health_check_target": "healthCheckTarget",
        "health_check_type": "healthCheckType",
        "hex_id": "hexId",
        "id": "id",
        "psk": "psk",
        "remote_id": "remoteId",
        "replay_protection": "replayProtection",
        "user_id": "userId",
    },
)
class IpsecTunnelConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cloudflare_endpoint: builtins.str,
        customer_endpoint: builtins.str,
        interface_address: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allow_null_cipher: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        fqdn_id: typing.Optional[builtins.str] = None,
        health_check_direction: typing.Optional[builtins.str] = None,
        health_check_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check_rate: typing.Optional[builtins.str] = None,
        health_check_target: typing.Optional[builtins.str] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        hex_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        psk: typing.Optional[builtins.str] = None,
        remote_id: typing.Optional[builtins.str] = None,
        replay_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cloudflare_endpoint: IP address assigned to the Cloudflare side of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#cloudflare_endpoint IpsecTunnel#cloudflare_endpoint}
        :param customer_endpoint: IP address assigned to the customer side of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#customer_endpoint IpsecTunnel#customer_endpoint}
        :param interface_address: 31-bit prefix (/31 in CIDR notation) supporting 2 hosts, one for each side of the tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#interface_address IpsecTunnel#interface_address}
        :param name: Name of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#name IpsecTunnel#name}
        :param account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#account_id IpsecTunnel#account_id}
        :param allow_null_cipher: Specifies if this tunnel may use a null cipher (ENCR_NULL) in Phase 2. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#allow_null_cipher IpsecTunnel#allow_null_cipher}
        :param description: An optional description of the IPsec tunnel. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#description IpsecTunnel#description}
        :param fqdn_id: ``remote_id`` in the form of a fqdn. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#fqdn_id IpsecTunnel#fqdn_id}
        :param health_check_direction: Specifies the direction for the health check. Available values: ``unidirectional``, ``bidirectional`` Default: ``unidirectional``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_direction IpsecTunnel#health_check_direction}
        :param health_check_enabled: Specifies if ICMP tunnel health checks are enabled. Default: ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_enabled IpsecTunnel#health_check_enabled}
        :param health_check_rate: Specifies the ICMP rate for the health check. Available values: ``low``, ``mid``, ``high`` Default: ``mid``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_rate IpsecTunnel#health_check_rate}
        :param health_check_target: The IP address of the customer endpoint that will receive tunnel health checks. Default: ``<customer_gre_endpoint>``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_target IpsecTunnel#health_check_target}
        :param health_check_type: Specifies the ICMP echo type for the health check (``request`` or ``reply``). Available values: ``request``, ``reply`` Default: ``reply``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_type IpsecTunnel#health_check_type}
        :param hex_id: ``remote_id`` as a hex string. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#hex_id IpsecTunnel#hex_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#id IpsecTunnel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param psk: Pre shared key to be used with the IPsec tunnel. If left unset, it will be autogenerated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#psk IpsecTunnel#psk}
        :param remote_id: ID to be used while setting up the IPsec tunnel. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#remote_id IpsecTunnel#remote_id}
        :param replay_protection: Specifies if replay protection is enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#replay_protection IpsecTunnel#replay_protection}
        :param user_id: ``remote_id`` in the form of an email address. This value is generated by cloudflare. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#user_id IpsecTunnel#user_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1443d9fd26bebc57d099d8bd3e1f4f8d67c555bcd7c1c511714206e044b1afb1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cloudflare_endpoint", value=cloudflare_endpoint, expected_type=type_hints["cloudflare_endpoint"])
            check_type(argname="argument customer_endpoint", value=customer_endpoint, expected_type=type_hints["customer_endpoint"])
            check_type(argname="argument interface_address", value=interface_address, expected_type=type_hints["interface_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument allow_null_cipher", value=allow_null_cipher, expected_type=type_hints["allow_null_cipher"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument fqdn_id", value=fqdn_id, expected_type=type_hints["fqdn_id"])
            check_type(argname="argument health_check_direction", value=health_check_direction, expected_type=type_hints["health_check_direction"])
            check_type(argname="argument health_check_enabled", value=health_check_enabled, expected_type=type_hints["health_check_enabled"])
            check_type(argname="argument health_check_rate", value=health_check_rate, expected_type=type_hints["health_check_rate"])
            check_type(argname="argument health_check_target", value=health_check_target, expected_type=type_hints["health_check_target"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument hex_id", value=hex_id, expected_type=type_hints["hex_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument psk", value=psk, expected_type=type_hints["psk"])
            check_type(argname="argument remote_id", value=remote_id, expected_type=type_hints["remote_id"])
            check_type(argname="argument replay_protection", value=replay_protection, expected_type=type_hints["replay_protection"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloudflare_endpoint": cloudflare_endpoint,
            "customer_endpoint": customer_endpoint,
            "interface_address": interface_address,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if account_id is not None:
            self._values["account_id"] = account_id
        if allow_null_cipher is not None:
            self._values["allow_null_cipher"] = allow_null_cipher
        if description is not None:
            self._values["description"] = description
        if fqdn_id is not None:
            self._values["fqdn_id"] = fqdn_id
        if health_check_direction is not None:
            self._values["health_check_direction"] = health_check_direction
        if health_check_enabled is not None:
            self._values["health_check_enabled"] = health_check_enabled
        if health_check_rate is not None:
            self._values["health_check_rate"] = health_check_rate
        if health_check_target is not None:
            self._values["health_check_target"] = health_check_target
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if hex_id is not None:
            self._values["hex_id"] = hex_id
        if id is not None:
            self._values["id"] = id
        if psk is not None:
            self._values["psk"] = psk
        if remote_id is not None:
            self._values["remote_id"] = remote_id
        if replay_protection is not None:
            self._values["replay_protection"] = replay_protection
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def cloudflare_endpoint(self) -> builtins.str:
        '''IP address assigned to the Cloudflare side of the IPsec tunnel.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#cloudflare_endpoint IpsecTunnel#cloudflare_endpoint}
        '''
        result = self._values.get("cloudflare_endpoint")
        assert result is not None, "Required property 'cloudflare_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_endpoint(self) -> builtins.str:
        '''IP address assigned to the customer side of the IPsec tunnel.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#customer_endpoint IpsecTunnel#customer_endpoint}
        '''
        result = self._values.get("customer_endpoint")
        assert result is not None, "Required property 'customer_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interface_address(self) -> builtins.str:
        '''31-bit prefix (/31 in CIDR notation) supporting 2 hosts, one for each side of the tunnel.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#interface_address IpsecTunnel#interface_address}
        '''
        result = self._values.get("interface_address")
        assert result is not None, "Required property 'interface_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the IPsec tunnel.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#name IpsecTunnel#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#account_id IpsecTunnel#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allow_null_cipher(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies if this tunnel may use a null cipher (ENCR_NULL) in Phase 2. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#allow_null_cipher IpsecTunnel#allow_null_cipher}
        '''
        result = self._values.get("allow_null_cipher")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the IPsec tunnel.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#description IpsecTunnel#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fqdn_id(self) -> typing.Optional[builtins.str]:
        '''``remote_id`` in the form of a fqdn. This value is generated by cloudflare.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#fqdn_id IpsecTunnel#fqdn_id}
        '''
        result = self._values.get("fqdn_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_direction(self) -> typing.Optional[builtins.str]:
        '''Specifies the direction for the health check. Available values: ``unidirectional``, ``bidirectional`` Default: ``unidirectional``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_direction IpsecTunnel#health_check_direction}
        '''
        result = self._values.get("health_check_direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies if ICMP tunnel health checks are enabled. Default: ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_enabled IpsecTunnel#health_check_enabled}
        '''
        result = self._values.get("health_check_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check_rate(self) -> typing.Optional[builtins.str]:
        '''Specifies the ICMP rate for the health check. Available values: ``low``, ``mid``, ``high`` Default: ``mid``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_rate IpsecTunnel#health_check_rate}
        '''
        result = self._values.get("health_check_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_target(self) -> typing.Optional[builtins.str]:
        '''The IP address of the customer endpoint that will receive tunnel health checks. Default: ``<customer_gre_endpoint>``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_target IpsecTunnel#health_check_target}
        '''
        result = self._values.get("health_check_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the ICMP echo type for the health check (``request`` or ``reply``). Available values: ``request``, ``reply`` Default: ``reply``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#health_check_type IpsecTunnel#health_check_type}
        '''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hex_id(self) -> typing.Optional[builtins.str]:
        '''``remote_id`` as a hex string. This value is generated by cloudflare.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#hex_id IpsecTunnel#hex_id}
        '''
        result = self._values.get("hex_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#id IpsecTunnel#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def psk(self) -> typing.Optional[builtins.str]:
        '''Pre shared key to be used with the IPsec tunnel. If left unset, it will be autogenerated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#psk IpsecTunnel#psk}
        '''
        result = self._values.get("psk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''ID to be used while setting up the IPsec tunnel. This value is generated by cloudflare.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#remote_id IpsecTunnel#remote_id}
        '''
        result = self._values.get("remote_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replay_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies if replay protection is enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#replay_protection IpsecTunnel#replay_protection}
        '''
        result = self._values.get("replay_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''``remote_id`` in the form of an email address. This value is generated by cloudflare.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ipsec_tunnel#user_id IpsecTunnel#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpsecTunnelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IpsecTunnel",
    "IpsecTunnelConfig",
]

publication.publish()

def _typecheckingstub__ca1b3e56ac7517da72e0f79208ea920dfeab531292da51ba1b9163a57d83f04b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cloudflare_endpoint: builtins.str,
    customer_endpoint: builtins.str,
    interface_address: builtins.str,
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    allow_null_cipher: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    fqdn_id: typing.Optional[builtins.str] = None,
    health_check_direction: typing.Optional[builtins.str] = None,
    health_check_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check_rate: typing.Optional[builtins.str] = None,
    health_check_target: typing.Optional[builtins.str] = None,
    health_check_type: typing.Optional[builtins.str] = None,
    hex_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    psk: typing.Optional[builtins.str] = None,
    remote_id: typing.Optional[builtins.str] = None,
    replay_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_id: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db04a4ed789ae861c04f83f86486e54c31b08abba6fb82bdd1a7d350428906f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de5a37c8e08d3e8ba523b5eb03edb5e7a63c70b4fd7d05cc6492540d46d410b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564bca3f42872d1f7bf6d5e39da0381b272d0a5e857825b4f51b2b601f712784(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a258b37536c627d455f9bfb82e0a91c26e8083bf1b07af8378c56b337e678d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05589e72a25bbd3766b87351b6a73a02ecde5ab814310b1adfc71cfcf595067e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23ff8040934f4a14ad16b7c564a8c0285a80d3fbe6af4700dba33fdca2f2b33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc92d0a8f7c3c519926ec4ed2a5ffc1022239a5e20e2e4340dbcbfd900621841(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be673b3e457d3e5067d9cc24acebf397b9c7779b542df116054cc0b0a14b370f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2067562cd61574a0df9ad18d40bb4153cfde0e42cbfddba1909cb25d4938501(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21be19939a649483c7f1ce2c73145e22a95c49bc94232aa360483819789d40f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7178761a8e0b71f26a69a26d9cb659912a6afe04dde576b74dfbcbf3b0394ed3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa01f96f8e91193acf6863e1d1871cb8bcd4d5e04df22df98046b006bae00cbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2ebd25b383116af614d36b5718f6d879d08b8fc0affa2b358f1281e67b00c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a76430fbd52017016629f079e11f1901b6b056d7d14744a8939793611281bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a84dfd6e30da71066ca70f0fc952e648a29c34e00f32ed2a6a58d96b3af9143(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42316ada419534ad06a5a9fab08d9c56cfb79d39c0ab826d24883cd4fa3118e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4a017df6ced225deb5bdcf508c1af69d0f0145a222e78c09514d93dfc7bde7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4bfd59910cd640d8b0621b0b1882cbc14b35f2b6449fe324858eee8826207f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8382a52091835929299e67a6928cfbe1c617335d4344f4d88398188d79c0160c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf4c962c56c6b0db71de36c986f2c434ea050f87b637efbbce8fe81f69345b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1443d9fd26bebc57d099d8bd3e1f4f8d67c555bcd7c1c511714206e044b1afb1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloudflare_endpoint: builtins.str,
    customer_endpoint: builtins.str,
    interface_address: builtins.str,
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    allow_null_cipher: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    fqdn_id: typing.Optional[builtins.str] = None,
    health_check_direction: typing.Optional[builtins.str] = None,
    health_check_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check_rate: typing.Optional[builtins.str] = None,
    health_check_target: typing.Optional[builtins.str] = None,
    health_check_type: typing.Optional[builtins.str] = None,
    hex_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    psk: typing.Optional[builtins.str] = None,
    remote_id: typing.Optional[builtins.str] = None,
    replay_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
