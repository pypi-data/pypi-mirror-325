r'''
# `cloudflare_ruleset`

Refer to the Terraform Registry for docs: [`cloudflare_ruleset`](https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset).
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


class Ruleset(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.Ruleset",
):
    '''Represents a {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset cloudflare_ruleset}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        kind: builtins.str,
        name: builtins.str,
        phase: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset cloudflare_ruleset} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param kind: Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``zone``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#kind Ruleset#kind}
        :param name: Name of the ruleset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        :param phase: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_config_settings``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_ratelimit``, ``http_request_cache_settings``, ``http_request_dynamic_redirect``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_origin``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_compression``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``magic_transit``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#phase Ruleset#phase}
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#account_id Ruleset#account_id}
        :param description: Brief summary of the ruleset and its intended use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#description Ruleset#description}
        :param rules: rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#zone_id Ruleset#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__976786290c680465b7503207e2760a89b7faab8f545d61010c5b231f989d5e9a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = RulesetConfig(
            kind=kind,
            name=name,
            phase=phase,
            account_id=account_id,
            description=description,
            rules=rules,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
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
        '''Generates CDKTF code for importing a Ruleset resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Ruleset to import.
        :param import_from_id: The id of the existing Ruleset that should be imported. Refer to the {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Ruleset to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9220a4ee626fa5b46efa9b641bf2923cc2fc05444a070651e7d2338b99871c5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881837c538b68bfed772ddae8847420413bdbc447c99cff9d5a54a1e04334cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "RulesetRulesList":
        return typing.cast("RulesetRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseInput")
    def phase_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phaseInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e80fb2673b8f294f1f67700c48de5631ba9d9c567cb81cb7c00d7163b475a0d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5dea1392d141168a91b4bd2001493954d20c1ea1a06814fdf6869dc5f96bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3350d0df37447458b9f40b63bffd161a6dcb0c965ebd5a4ae057b97f5cea4d12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e821cae1ccdf5e020c021afe5d57e5d2a88a5d524b4ba61ad522d8842625cfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phase")
    def phase(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phase"))

    @phase.setter
    def phase(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bad56699a9f7b700c704be44e1189db8b97da2bf789aafdc922b8e8e400427)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phase", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f15432da9ba29f74d3ef770a089c57008555d54590ae3e98cc690d0ba5f956b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "kind": "kind",
        "name": "name",
        "phase": "phase",
        "account_id": "accountId",
        "description": "description",
        "rules": "rules",
        "zone_id": "zoneId",
    },
)
class RulesetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        kind: builtins.str,
        name: builtins.str,
        phase: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param kind: Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``zone``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#kind Ruleset#kind}
        :param name: Name of the ruleset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        :param phase: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_config_settings``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_ratelimit``, ``http_request_cache_settings``, ``http_request_dynamic_redirect``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_origin``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_compression``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``magic_transit``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#phase Ruleset#phase}
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#account_id Ruleset#account_id}
        :param description: Brief summary of the ruleset and its intended use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#description Ruleset#description}
        :param rules: rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#zone_id Ruleset#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c5cd7dc19dc7eb2bb1a771ec52756f2b48fb9dffe752e856e8e778bd43737a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phase", value=phase, expected_type=type_hints["phase"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
            "name": name,
            "phase": phase,
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
        if description is not None:
            self._values["description"] = description
        if rules is not None:
            self._values["rules"] = rules
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def kind(self) -> builtins.str:
        '''Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``zone``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#kind Ruleset#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the ruleset.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phase(self) -> builtins.str:
        '''Point in the request/response lifecycle where the ruleset will be created.

        Available values: ``ddos_l4``, ``ddos_l7``, ``http_config_settings``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_ratelimit``, ``http_request_cache_settings``, ``http_request_dynamic_redirect``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_origin``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_compression``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``magic_transit``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#phase Ruleset#phase}
        '''
        result = self._values.get("phase")
        assert result is not None, "Required property 'phase' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#account_id Ruleset#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Brief summary of the ruleset and its intended use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#description Ruleset#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRules"]]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRules"]]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#zone_id Ruleset#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRules",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "action": "action",
        "action_parameters": "actionParameters",
        "description": "description",
        "enabled": "enabled",
        "exposed_credential_check": "exposedCredentialCheck",
        "logging": "logging",
        "ratelimit": "ratelimit",
        "ref": "ref",
    },
)
class RulesetRules:
    def __init__(
        self,
        *,
        expression: builtins.str,
        action: typing.Optional[builtins.str] = None,
        action_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        exposed_credential_check: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesExposedCredentialCheck", typing.Dict[builtins.str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesLogging", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ratelimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesRatelimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ref: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Criteria for an HTTP request to trigger the ruleset rule action. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        :param action: Action to perform in the ruleset rule. Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        :param action_parameters: action_parameters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action_parameters Ruleset#action_parameters}
        :param description: Brief summary of the ruleset rule and its intended use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#description Ruleset#description}
        :param enabled: Whether the rule is active. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        :param exposed_credential_check: exposed_credential_check block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exposed_credential_check Ruleset#exposed_credential_check}
        :param logging: logging block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#logging Ruleset#logging}
        :param ratelimit: ratelimit block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ratelimit Ruleset#ratelimit}
        :param ref: Rule reference. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ref Ruleset#ref}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cca2253f99d951ccb4d27f919867272a1d49d30084abd0aa98f9315a79b791da)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument action_parameters", value=action_parameters, expected_type=type_hints["action_parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exposed_credential_check", value=exposed_credential_check, expected_type=type_hints["exposed_credential_check"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument ratelimit", value=ratelimit, expected_type=type_hints["ratelimit"])
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
        }
        if action is not None:
            self._values["action"] = action
        if action_parameters is not None:
            self._values["action_parameters"] = action_parameters
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if exposed_credential_check is not None:
            self._values["exposed_credential_check"] = exposed_credential_check
        if logging is not None:
            self._values["logging"] = logging
        if ratelimit is not None:
            self._values["ratelimit"] = ratelimit
        if ref is not None:
            self._values["ref"] = ref

    @builtins.property
    def expression(self) -> builtins.str:
        '''Criteria for an HTTP request to trigger the ruleset rule action.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the ruleset rule.

        Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParameters"]]]:
        '''action_parameters block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action_parameters Ruleset#action_parameters}
        '''
        result = self._values.get("action_parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParameters"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Brief summary of the ruleset rule and its intended use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#description Ruleset#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the rule is active.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def exposed_credential_check(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesExposedCredentialCheck"]]]:
        '''exposed_credential_check block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exposed_credential_check Ruleset#exposed_credential_check}
        '''
        result = self._values.get("exposed_credential_check")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesExposedCredentialCheck"]]], result)

    @builtins.property
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesLogging"]]]:
        '''logging block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#logging Ruleset#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesLogging"]]], result)

    @builtins.property
    def ratelimit(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesRatelimit"]]]:
        '''ratelimit block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ratelimit Ruleset#ratelimit}
        '''
        result = self._values.get("ratelimit")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesRatelimit"]]], result)

    @builtins.property
    def ref(self) -> typing.Optional[builtins.str]:
        '''Rule reference.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ref Ruleset#ref}
        '''
        result = self._values.get("ref")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParameters",
    jsii_struct_bases=[],
    name_mapping={
        "additional_cacheable_ports": "additionalCacheablePorts",
        "algorithms": "algorithms",
        "automatic_https_rewrites": "automaticHttpsRewrites",
        "autominify": "autominify",
        "bic": "bic",
        "browser_ttl": "browserTtl",
        "cache": "cache",
        "cache_key": "cacheKey",
        "cache_reserve": "cacheReserve",
        "content": "content",
        "content_type": "contentType",
        "cookie_fields": "cookieFields",
        "disable_apps": "disableApps",
        "disable_railgun": "disableRailgun",
        "disable_rum": "disableRum",
        "disable_zaraz": "disableZaraz",
        "edge_ttl": "edgeTtl",
        "email_obfuscation": "emailObfuscation",
        "fonts": "fonts",
        "from_list": "fromList",
        "from_value": "fromValue",
        "headers": "headers",
        "host_header": "hostHeader",
        "hotlink_protection": "hotlinkProtection",
        "id": "id",
        "increment": "increment",
        "matched_data": "matchedData",
        "mirage": "mirage",
        "opportunistic_encryption": "opportunisticEncryption",
        "origin": "origin",
        "origin_cache_control": "originCacheControl",
        "origin_error_page_passthru": "originErrorPagePassthru",
        "overrides": "overrides",
        "phases": "phases",
        "polish": "polish",
        "products": "products",
        "read_timeout": "readTimeout",
        "request_fields": "requestFields",
        "respect_strong_etags": "respectStrongEtags",
        "response": "response",
        "response_fields": "responseFields",
        "rocket_loader": "rocketLoader",
        "rules": "rules",
        "ruleset": "ruleset",
        "rulesets": "rulesets",
        "security_level": "securityLevel",
        "server_side_excludes": "serverSideExcludes",
        "serve_stale": "serveStale",
        "sni": "sni",
        "ssl": "ssl",
        "status_code": "statusCode",
        "sxg": "sxg",
        "uri": "uri",
    },
)
class RulesetRulesActionParameters:
    def __init__(
        self,
        *,
        additional_cacheable_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
        algorithms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersAlgorithms", typing.Dict[builtins.str, typing.Any]]]]] = None,
        automatic_https_rewrites: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        autominify: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersAutominify", typing.Dict[builtins.str, typing.Any]]]]] = None,
        bic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        browser_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersBrowserTtl", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cache_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cache_reserve: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheReserve", typing.Dict[builtins.str, typing.Any]]]]] = None,
        content: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        cookie_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        disable_apps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_railgun: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_rum: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_zaraz: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        edge_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtl", typing.Dict[builtins.str, typing.Any]]]]] = None,
        email_obfuscation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fonts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        from_list: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersFromListStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        from_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersFromValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
        headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        host_header: typing.Optional[builtins.str] = None,
        hotlink_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        increment: typing.Optional[jsii.Number] = None,
        matched_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersMatchedData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mirage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        opportunistic_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        origin: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOrigin", typing.Dict[builtins.str, typing.Any]]]]] = None,
        origin_cache_control: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        origin_error_page_passthru: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        overrides: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverrides", typing.Dict[builtins.str, typing.Any]]]]] = None,
        phases: typing.Optional[typing.Sequence[builtins.str]] = None,
        polish: typing.Optional[builtins.str] = None,
        products: typing.Optional[typing.Sequence[builtins.str]] = None,
        read_timeout: typing.Optional[jsii.Number] = None,
        request_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        respect_strong_etags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersResponse", typing.Dict[builtins.str, typing.Any]]]]] = None,
        response_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        rocket_loader: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rules: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ruleset: typing.Optional[builtins.str] = None,
        rulesets: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_excludes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        serve_stale: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersServeStale", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sni: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersSni", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ssl: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
        sxg: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        uri: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUri", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_cacheable_ports: Specifies uncommon ports to allow cacheable assets to be served from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#additional_cacheable_ports Ruleset#additional_cacheable_ports}
        :param algorithms: algorithms block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#algorithms Ruleset#algorithms}
        :param automatic_https_rewrites: Turn on or off Cloudflare Automatic HTTPS rewrites. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#automatic_https_rewrites Ruleset#automatic_https_rewrites}
        :param autominify: autominify block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#autominify Ruleset#autominify}
        :param bic: Inspect the visitor's browser for headers commonly associated with spammers and certain bots. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#bic Ruleset#bic}
        :param browser_ttl: browser_ttl block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#browser_ttl Ruleset#browser_ttl}
        :param cache: Whether to cache if expression matches. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache Ruleset#cache}
        :param cache_key: cache_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_key Ruleset#cache_key}
        :param cache_reserve: cache_reserve block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_reserve Ruleset#cache_reserve}
        :param content: Content of the custom error response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content Ruleset#content}
        :param content_type: Content-Type of the custom error response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content_type Ruleset#content_type}
        :param cookie_fields: List of cookie values to include as part of custom fields logging. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cookie_fields Ruleset#cookie_fields}
        :param disable_apps: Turn off all active Cloudflare Apps. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_apps Ruleset#disable_apps}
        :param disable_railgun: Turn off railgun feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_railgun Ruleset#disable_railgun}
        :param disable_rum: Turn off RUM feature. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_rum Ruleset#disable_rum}
        :param disable_zaraz: Turn off zaraz feature. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_zaraz Ruleset#disable_zaraz}
        :param edge_ttl: edge_ttl block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#edge_ttl Ruleset#edge_ttl}
        :param email_obfuscation: Turn on or off the Cloudflare Email Obfuscation feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#email_obfuscation Ruleset#email_obfuscation}
        :param fonts: Toggle fonts. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#fonts Ruleset#fonts}
        :param from_list: from_list block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from_list Ruleset#from_list}
        :param from_value: from_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from_value Ruleset#from_value}
        :param headers: headers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#headers Ruleset#headers}
        :param host_header: Host Header that request origin receives. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host_header Ruleset#host_header}
        :param hotlink_protection: Turn on or off the hotlink protection feature. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#hotlink_protection Ruleset#hotlink_protection}
        :param id: Identifier of the action parameter to modify. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#id Ruleset#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param increment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#increment Ruleset#increment}.
        :param matched_data: matched_data block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#matched_data Ruleset#matched_data}
        :param mirage: Turn on or off Cloudflare Mirage of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mirage Ruleset#mirage}
        :param opportunistic_encryption: Turn on or off the Cloudflare Opportunistic Encryption feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#opportunistic_encryption Ruleset#opportunistic_encryption}
        :param origin: origin block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin Ruleset#origin}
        :param origin_cache_control: Enable or disable the use of a more compliant Cache Control parsing mechanism, enabled by default for most zones. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin_cache_control Ruleset#origin_cache_control}
        :param origin_error_page_passthru: Pass-through error page for origin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin_error_page_passthru Ruleset#origin_error_page_passthru}
        :param overrides: overrides block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#overrides Ruleset#overrides}
        :param phases: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_config_settings``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_ratelimit``, ``http_request_cache_settings``, ``http_request_dynamic_redirect``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_origin``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_compression``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``magic_transit``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#phases Ruleset#phases}
        :param polish: Apply options from the Polish feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#polish Ruleset#polish}
        :param products: Products to target with the actions. Available values: ``bic``, ``hot``, ``ratelimit``, ``securityLevel``, ``uablock``, ``waf``, ``zonelockdown``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#products Ruleset#products}
        :param read_timeout: Specifies a maximum timeout for reading content from an origin server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#read_timeout Ruleset#read_timeout}
        :param request_fields: List of request headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#request_fields Ruleset#request_fields}
        :param respect_strong_etags: Respect strong ETags. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#respect_strong_etags Ruleset#respect_strong_etags}
        :param response: response block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#response Ruleset#response}
        :param response_fields: List of response headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#response_fields Ruleset#response_fields}
        :param rocket_loader: Turn on or off Cloudflare Rocket Loader in the Cloudflare Speed app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rocket_loader Ruleset#rocket_loader}
        :param rules: Map of managed WAF rule ID to comma-delimited string of ruleset rule IDs. Example: ``rules = { "efb7b8c949ac4650a09736fc376e9aee" = "5de7edfa648c4d6891dc3e7f84534ffa,e3a567afc347477d9702d9047e97d760" }``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        :param ruleset: Which ruleset ID to target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ruleset Ruleset#ruleset}
        :param rulesets: List of managed WAF rule IDs to target. Only valid when the ``"action"`` is set to skip. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rulesets Ruleset#rulesets}
        :param security_level: Control options for the Security Level feature from the Security app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#security_level Ruleset#security_level}
        :param server_side_excludes: Turn on or off the Server Side Excludes feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#server_side_excludes Ruleset#server_side_excludes}
        :param serve_stale: serve_stale block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#serve_stale Ruleset#serve_stale}
        :param sni: sni block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sni Ruleset#sni}
        :param ssl: Control options for the SSL feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ssl Ruleset#ssl}
        :param status_code: HTTP status code of the custom error response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        :param sxg: Turn on or off the SXG feature. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sxg Ruleset#sxg}
        :param uri: uri block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#uri Ruleset#uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d6b0152ba2e2b3e20a1543e04b3a6086c9466575dc6ccbbeb755c66c3a0f146)
            check_type(argname="argument additional_cacheable_ports", value=additional_cacheable_ports, expected_type=type_hints["additional_cacheable_ports"])
            check_type(argname="argument algorithms", value=algorithms, expected_type=type_hints["algorithms"])
            check_type(argname="argument automatic_https_rewrites", value=automatic_https_rewrites, expected_type=type_hints["automatic_https_rewrites"])
            check_type(argname="argument autominify", value=autominify, expected_type=type_hints["autominify"])
            check_type(argname="argument bic", value=bic, expected_type=type_hints["bic"])
            check_type(argname="argument browser_ttl", value=browser_ttl, expected_type=type_hints["browser_ttl"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument cache_key", value=cache_key, expected_type=type_hints["cache_key"])
            check_type(argname="argument cache_reserve", value=cache_reserve, expected_type=type_hints["cache_reserve"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument cookie_fields", value=cookie_fields, expected_type=type_hints["cookie_fields"])
            check_type(argname="argument disable_apps", value=disable_apps, expected_type=type_hints["disable_apps"])
            check_type(argname="argument disable_railgun", value=disable_railgun, expected_type=type_hints["disable_railgun"])
            check_type(argname="argument disable_rum", value=disable_rum, expected_type=type_hints["disable_rum"])
            check_type(argname="argument disable_zaraz", value=disable_zaraz, expected_type=type_hints["disable_zaraz"])
            check_type(argname="argument edge_ttl", value=edge_ttl, expected_type=type_hints["edge_ttl"])
            check_type(argname="argument email_obfuscation", value=email_obfuscation, expected_type=type_hints["email_obfuscation"])
            check_type(argname="argument fonts", value=fonts, expected_type=type_hints["fonts"])
            check_type(argname="argument from_list", value=from_list, expected_type=type_hints["from_list"])
            check_type(argname="argument from_value", value=from_value, expected_type=type_hints["from_value"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument hotlink_protection", value=hotlink_protection, expected_type=type_hints["hotlink_protection"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument increment", value=increment, expected_type=type_hints["increment"])
            check_type(argname="argument matched_data", value=matched_data, expected_type=type_hints["matched_data"])
            check_type(argname="argument mirage", value=mirage, expected_type=type_hints["mirage"])
            check_type(argname="argument opportunistic_encryption", value=opportunistic_encryption, expected_type=type_hints["opportunistic_encryption"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument origin_cache_control", value=origin_cache_control, expected_type=type_hints["origin_cache_control"])
            check_type(argname="argument origin_error_page_passthru", value=origin_error_page_passthru, expected_type=type_hints["origin_error_page_passthru"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument phases", value=phases, expected_type=type_hints["phases"])
            check_type(argname="argument polish", value=polish, expected_type=type_hints["polish"])
            check_type(argname="argument products", value=products, expected_type=type_hints["products"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
            check_type(argname="argument request_fields", value=request_fields, expected_type=type_hints["request_fields"])
            check_type(argname="argument respect_strong_etags", value=respect_strong_etags, expected_type=type_hints["respect_strong_etags"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            check_type(argname="argument response_fields", value=response_fields, expected_type=type_hints["response_fields"])
            check_type(argname="argument rocket_loader", value=rocket_loader, expected_type=type_hints["rocket_loader"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument ruleset", value=ruleset, expected_type=type_hints["ruleset"])
            check_type(argname="argument rulesets", value=rulesets, expected_type=type_hints["rulesets"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument server_side_excludes", value=server_side_excludes, expected_type=type_hints["server_side_excludes"])
            check_type(argname="argument serve_stale", value=serve_stale, expected_type=type_hints["serve_stale"])
            check_type(argname="argument sni", value=sni, expected_type=type_hints["sni"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument sxg", value=sxg, expected_type=type_hints["sxg"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_cacheable_ports is not None:
            self._values["additional_cacheable_ports"] = additional_cacheable_ports
        if algorithms is not None:
            self._values["algorithms"] = algorithms
        if automatic_https_rewrites is not None:
            self._values["automatic_https_rewrites"] = automatic_https_rewrites
        if autominify is not None:
            self._values["autominify"] = autominify
        if bic is not None:
            self._values["bic"] = bic
        if browser_ttl is not None:
            self._values["browser_ttl"] = browser_ttl
        if cache is not None:
            self._values["cache"] = cache
        if cache_key is not None:
            self._values["cache_key"] = cache_key
        if cache_reserve is not None:
            self._values["cache_reserve"] = cache_reserve
        if content is not None:
            self._values["content"] = content
        if content_type is not None:
            self._values["content_type"] = content_type
        if cookie_fields is not None:
            self._values["cookie_fields"] = cookie_fields
        if disable_apps is not None:
            self._values["disable_apps"] = disable_apps
        if disable_railgun is not None:
            self._values["disable_railgun"] = disable_railgun
        if disable_rum is not None:
            self._values["disable_rum"] = disable_rum
        if disable_zaraz is not None:
            self._values["disable_zaraz"] = disable_zaraz
        if edge_ttl is not None:
            self._values["edge_ttl"] = edge_ttl
        if email_obfuscation is not None:
            self._values["email_obfuscation"] = email_obfuscation
        if fonts is not None:
            self._values["fonts"] = fonts
        if from_list is not None:
            self._values["from_list"] = from_list
        if from_value is not None:
            self._values["from_value"] = from_value
        if headers is not None:
            self._values["headers"] = headers
        if host_header is not None:
            self._values["host_header"] = host_header
        if hotlink_protection is not None:
            self._values["hotlink_protection"] = hotlink_protection
        if id is not None:
            self._values["id"] = id
        if increment is not None:
            self._values["increment"] = increment
        if matched_data is not None:
            self._values["matched_data"] = matched_data
        if mirage is not None:
            self._values["mirage"] = mirage
        if opportunistic_encryption is not None:
            self._values["opportunistic_encryption"] = opportunistic_encryption
        if origin is not None:
            self._values["origin"] = origin
        if origin_cache_control is not None:
            self._values["origin_cache_control"] = origin_cache_control
        if origin_error_page_passthru is not None:
            self._values["origin_error_page_passthru"] = origin_error_page_passthru
        if overrides is not None:
            self._values["overrides"] = overrides
        if phases is not None:
            self._values["phases"] = phases
        if polish is not None:
            self._values["polish"] = polish
        if products is not None:
            self._values["products"] = products
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout
        if request_fields is not None:
            self._values["request_fields"] = request_fields
        if respect_strong_etags is not None:
            self._values["respect_strong_etags"] = respect_strong_etags
        if response is not None:
            self._values["response"] = response
        if response_fields is not None:
            self._values["response_fields"] = response_fields
        if rocket_loader is not None:
            self._values["rocket_loader"] = rocket_loader
        if rules is not None:
            self._values["rules"] = rules
        if ruleset is not None:
            self._values["ruleset"] = ruleset
        if rulesets is not None:
            self._values["rulesets"] = rulesets
        if security_level is not None:
            self._values["security_level"] = security_level
        if server_side_excludes is not None:
            self._values["server_side_excludes"] = server_side_excludes
        if serve_stale is not None:
            self._values["serve_stale"] = serve_stale
        if sni is not None:
            self._values["sni"] = sni
        if ssl is not None:
            self._values["ssl"] = ssl
        if status_code is not None:
            self._values["status_code"] = status_code
        if sxg is not None:
            self._values["sxg"] = sxg
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def additional_cacheable_ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Specifies uncommon ports to allow cacheable assets to be served from.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#additional_cacheable_ports Ruleset#additional_cacheable_ports}
        '''
        result = self._values.get("additional_cacheable_ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def algorithms(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersAlgorithms"]]]:
        '''algorithms block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#algorithms Ruleset#algorithms}
        '''
        result = self._values.get("algorithms")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersAlgorithms"]]], result)

    @builtins.property
    def automatic_https_rewrites(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off Cloudflare Automatic HTTPS rewrites.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#automatic_https_rewrites Ruleset#automatic_https_rewrites}
        '''
        result = self._values.get("automatic_https_rewrites")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def autominify(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersAutominify"]]]:
        '''autominify block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#autominify Ruleset#autominify}
        '''
        result = self._values.get("autominify")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersAutominify"]]], result)

    @builtins.property
    def bic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Inspect the visitor's browser for headers commonly associated with spammers and certain bots.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#bic Ruleset#bic}
        '''
        result = self._values.get("bic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def browser_ttl(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersBrowserTtl"]]]:
        '''browser_ttl block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#browser_ttl Ruleset#browser_ttl}
        '''
        result = self._values.get("browser_ttl")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersBrowserTtl"]]], result)

    @builtins.property
    def cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to cache if expression matches.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache Ruleset#cache}
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cache_key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKey"]]]:
        '''cache_key block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_key Ruleset#cache_key}
        '''
        result = self._values.get("cache_key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKey"]]], result)

    @builtins.property
    def cache_reserve(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheReserve"]]]:
        '''cache_reserve block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_reserve Ruleset#cache_reserve}
        '''
        result = self._values.get("cache_reserve")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheReserve"]]], result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Content of the custom error response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content Ruleset#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Content-Type of the custom error response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content_type Ruleset#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cookie_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookie values to include as part of custom fields logging.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cookie_fields Ruleset#cookie_fields}
        '''
        result = self._values.get("cookie_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disable_apps(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn off all active Cloudflare Apps.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_apps Ruleset#disable_apps}
        '''
        result = self._values.get("disable_apps")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_railgun(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn off railgun feature of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_railgun Ruleset#disable_railgun}
        '''
        result = self._values.get("disable_railgun")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_rum(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn off RUM feature.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_rum Ruleset#disable_rum}
        '''
        result = self._values.get("disable_rum")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_zaraz(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn off zaraz feature.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_zaraz Ruleset#disable_zaraz}
        '''
        result = self._values.get("disable_zaraz")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def edge_ttl(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtl"]]]:
        '''edge_ttl block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#edge_ttl Ruleset#edge_ttl}
        '''
        result = self._values.get("edge_ttl")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtl"]]], result)

    @builtins.property
    def email_obfuscation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off the Cloudflare Email Obfuscation feature of the Cloudflare Scrape Shield app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#email_obfuscation Ruleset#email_obfuscation}
        '''
        result = self._values.get("email_obfuscation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fonts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Toggle fonts.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#fonts Ruleset#fonts}
        '''
        result = self._values.get("fonts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def from_list(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromListStruct"]]]:
        '''from_list block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from_list Ruleset#from_list}
        '''
        result = self._values.get("from_list")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromListStruct"]]], result)

    @builtins.property
    def from_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValue"]]]:
        '''from_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from_value Ruleset#from_value}
        '''
        result = self._values.get("from_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValue"]]], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#headers Ruleset#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersHeaders"]]], result)

    @builtins.property
    def host_header(self) -> typing.Optional[builtins.str]:
        '''Host Header that request origin receives.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host_header Ruleset#host_header}
        '''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hotlink_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off the hotlink protection feature.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#hotlink_protection Ruleset#hotlink_protection}
        '''
        result = self._values.get("hotlink_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the action parameter to modify.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#id Ruleset#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def increment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#increment Ruleset#increment}.'''
        result = self._values.get("increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matched_data(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersMatchedData"]]]:
        '''matched_data block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#matched_data Ruleset#matched_data}
        '''
        result = self._values.get("matched_data")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersMatchedData"]]], result)

    @builtins.property
    def mirage(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off Cloudflare Mirage of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mirage Ruleset#mirage}
        '''
        result = self._values.get("mirage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def opportunistic_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off the Cloudflare Opportunistic Encryption feature of the Edge Certificates tab in the Cloudflare SSL/TLS app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#opportunistic_encryption Ruleset#opportunistic_encryption}
        '''
        result = self._values.get("opportunistic_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def origin(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOrigin"]]]:
        '''origin block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin Ruleset#origin}
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOrigin"]]], result)

    @builtins.property
    def origin_cache_control(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable or disable the use of a more compliant Cache Control parsing mechanism, enabled by default for most zones.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin_cache_control Ruleset#origin_cache_control}
        '''
        result = self._values.get("origin_cache_control")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def origin_error_page_passthru(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Pass-through error page for origin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin_error_page_passthru Ruleset#origin_error_page_passthru}
        '''
        result = self._values.get("origin_error_page_passthru")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def overrides(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverrides"]]]:
        '''overrides block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#overrides Ruleset#overrides}
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverrides"]]], result)

    @builtins.property
    def phases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Point in the request/response lifecycle where the ruleset will be created.

        Available values: ``ddos_l4``, ``ddos_l7``, ``http_config_settings``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_ratelimit``, ``http_request_cache_settings``, ``http_request_dynamic_redirect``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_origin``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_compression``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``magic_transit``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#phases Ruleset#phases}
        '''
        result = self._values.get("phases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def polish(self) -> typing.Optional[builtins.str]:
        '''Apply options from the Polish feature of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#polish Ruleset#polish}
        '''
        result = self._values.get("polish")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def products(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Products to target with the actions. Available values: ``bic``, ``hot``, ``ratelimit``, ``securityLevel``, ``uablock``, ``waf``, ``zonelockdown``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#products Ruleset#products}
        '''
        result = self._values.get("products")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[jsii.Number]:
        '''Specifies a maximum timeout for reading content from an origin server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#read_timeout Ruleset#read_timeout}
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of request headers to include as part of custom fields logging, in lowercase.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#request_fields Ruleset#request_fields}
        '''
        result = self._values.get("request_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def respect_strong_etags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Respect strong ETags.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#respect_strong_etags Ruleset#respect_strong_etags}
        '''
        result = self._values.get("respect_strong_etags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def response(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]]:
        '''response block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#response Ruleset#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]], result)

    @builtins.property
    def response_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of response headers to include as part of custom fields logging, in lowercase.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#response_fields Ruleset#response_fields}
        '''
        result = self._values.get("response_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rocket_loader(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off Cloudflare Rocket Loader in the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rocket_loader Ruleset#rocket_loader}
        '''
        result = self._values.get("rocket_loader")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of managed WAF rule ID to comma-delimited string of ruleset rule IDs.

        Example: ``rules = { "efb7b8c949ac4650a09736fc376e9aee" = "5de7edfa648c4d6891dc3e7f84534ffa,e3a567afc347477d9702d9047e97d760" }``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ruleset(self) -> typing.Optional[builtins.str]:
        '''Which ruleset ID to target.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ruleset Ruleset#ruleset}
        '''
        result = self._values.get("ruleset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rulesets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of managed WAF rule IDs to target. Only valid when the ``"action"`` is set to skip.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rulesets Ruleset#rulesets}
        '''
        result = self._values.get("rulesets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Control options for the Security Level feature from the Security app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#security_level Ruleset#security_level}
        '''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_excludes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off the Server Side Excludes feature of the Cloudflare Scrape Shield app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#server_side_excludes Ruleset#server_side_excludes}
        '''
        result = self._values.get("server_side_excludes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def serve_stale(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersServeStale"]]]:
        '''serve_stale block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#serve_stale Ruleset#serve_stale}
        '''
        result = self._values.get("serve_stale")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersServeStale"]]], result)

    @builtins.property
    def sni(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersSni"]]]:
        '''sni block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sni Ruleset#sni}
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersSni"]]], result)

    @builtins.property
    def ssl(self) -> typing.Optional[builtins.str]:
        '''Control options for the SSL feature of the Edge Certificates tab in the Cloudflare SSL/TLS app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ssl Ruleset#ssl}
        '''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''HTTP status code of the custom error response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sxg(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Turn on or off the SXG feature.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sxg Ruleset#sxg}
        '''
        result = self._values.get("sxg")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def uri(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUri"]]]:
        '''uri block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#uri Ruleset#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUri"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAlgorithms",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class RulesetRulesActionParametersAlgorithms:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Name of the compression algorithm to use. Available values: ``zstd``, ``gzip``, ``brotli``, ``auto``, ``default``, ``none``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e0262db6c09550d44d4c025ce790ddd6d039f1166034a90a652c14970d71f0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the compression algorithm to use. Available values: ``zstd``, ``gzip``, ``brotli``, ``auto``, ``default``, ``none``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersAlgorithms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersAlgorithmsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAlgorithmsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab76d3bcacbae8dbd6d7d039f95a5b1951428d72e784d198e61ca5103b09cb5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersAlgorithmsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1451c3add3e56fdb117a400066b42fd2cdec02a34bb9780d2682fd72f28926bb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersAlgorithmsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb28cfe914ce1a99927f2b582f58cf638aa08351db03b87d9d87012c73f63380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e44bdf5c2a6eaa4c2d73a245413b3f39f4c9df40c77dfd1d3574f1b662c92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8896d4d9b26233a122db109114d50563519397456323b2b07f1627653f8ceede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9217775ff19fe799a909d4e61c10296b4d72735af343ba953508c8d86ae6cf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersAlgorithmsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAlgorithmsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f250fa9a8f3a9ebfab37548a40a5793a53a1e88a09e9970ccc65e6e9259c44)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a1b6f08425a7b315a07742c073c033e7548e5d0659bb92db1eb99459e22365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAlgorithms]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAlgorithms]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAlgorithms]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4531dfdbd831c864773006b1406d7157fa4a2ab3c94b3935a51ac7a0b7193cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominify",
    jsii_struct_bases=[],
    name_mapping={"css": "css", "html": "html", "js": "js"},
)
class RulesetRulesActionParametersAutominify:
    def __init__(
        self,
        *,
        css: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        html: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        js: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param css: CSS minification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#css Ruleset#css}
        :param html: HTML minification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#html Ruleset#html}
        :param js: JS minification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#js Ruleset#js}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00900fd4560c9b2410c168ed6fd981a9672e97d2d001b9fa2a687f864db0e119)
            check_type(argname="argument css", value=css, expected_type=type_hints["css"])
            check_type(argname="argument html", value=html, expected_type=type_hints["html"])
            check_type(argname="argument js", value=js, expected_type=type_hints["js"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if css is not None:
            self._values["css"] = css
        if html is not None:
            self._values["html"] = html
        if js is not None:
            self._values["js"] = js

    @builtins.property
    def css(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''CSS minification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#css Ruleset#css}
        '''
        result = self._values.get("css")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def html(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''HTML minification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#html Ruleset#html}
        '''
        result = self._values.get("html")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def js(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''JS minification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#js Ruleset#js}
        '''
        result = self._values.get("js")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersAutominify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersAutominifyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominifyList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7212c344c8c084ef7b27a7cdc3b3c6c87a75d5960c83fdd98ab354b44b29130e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersAutominifyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a363f084aab67fe73e37f8b04d652cc76ef79592aabf569546cbc880987ac3e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersAutominifyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b9a0a7420995e24dbb0ac0390152f22c6cc48a4871f180037b49cca423227b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c16e153a9587a76abd192d0be4ed2ca4e6de13c04f4f1cb7b7efaf729db71e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a39560922b1326bfd90d8a55e817a5248bdfe721128b4be0e039e1e2d702239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13867b203784083654161e3f10ad54f0779e23e3bcba05149830b7ee28f6e25d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersAutominifyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominifyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859ebfff2651399a8ff0a9f49df2a4f6478db32f9fd5544ddcfc540e4cf5a9dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCss")
    def reset_css(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCss", []))

    @jsii.member(jsii_name="resetHtml")
    def reset_html(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHtml", []))

    @jsii.member(jsii_name="resetJs")
    def reset_js(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJs", []))

    @builtins.property
    @jsii.member(jsii_name="cssInput")
    def css_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cssInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlInput")
    def html_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "htmlInput"))

    @builtins.property
    @jsii.member(jsii_name="jsInput")
    def js_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "jsInput"))

    @builtins.property
    @jsii.member(jsii_name="css")
    def css(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "css"))

    @css.setter
    def css(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7066d2d93aa6d9388f0f368c6cc12befea1199d70139d434f089abd6c285cafe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "css", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="html")
    def html(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "html"))

    @html.setter
    def html(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c36832329b69f82c2fc23be23a95f5ea6bf8b9c38062fe9522aa275469f84cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "html", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="js")
    def js(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "js"))

    @js.setter
    def js(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21dd89f47240bc2fc27119bbde218ceccf2902aa5b37e2eaedff2db2ae48c63b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "js", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAutominify]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAutominify]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAutominify]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972808188d2aefcf0e85e9f88bd170d2aaca612ec6fcb93884b4834c929c70b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersBrowserTtl",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "default": "default"},
)
class RulesetRulesActionParametersBrowserTtl:
    def __init__(
        self,
        *,
        mode: builtins.str,
        default: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Mode of the browser TTL. Available values: ``override_origin``, ``respect_origin``, ``bypass``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mode Ruleset#mode}
        :param default: Default browser TTL. This value is required when override_origin is set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#default Ruleset#default}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64155021267b0d4e14762908aa9c7fc518abf5d99cd0bf32b6a0d6b3c61693c6)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
        }
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode of the browser TTL. Available values: ``override_origin``, ``respect_origin``, ``bypass``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mode Ruleset#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[jsii.Number]:
        '''Default browser TTL. This value is required when override_origin is set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#default Ruleset#default}
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersBrowserTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersBrowserTtlList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersBrowserTtlList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7502e06ddedacb72a2014444a0b76a699761f4b69334238a699fe785bdfd5a4e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersBrowserTtlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f4e30dbc8117add7273f12f3d239f6452ed8732c348db3959b06d552b0299f2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersBrowserTtlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d437f31ace399c5c0f597176188a65277ffb0e8361acaabd1868542064dc52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12e9d5389461020470fc87ef5587d3e5e2b6140103d06d94a79a921dcf52b08b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b2cb1876ee02d13cee257ab25d2049be8bf31d41f6b078e18104c45f9295df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c23889d06fa1cf6aed1d21a3fbf0a028fa173b359b8121e8b89d51960863c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersBrowserTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersBrowserTtlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618e0e995f1c33f56cbd28afb0b26919c2a30a9fdb42628bc01383c9ee2ba9a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "default"))

    @default.setter
    def default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a5c6b36d041498713a003ebb7246285cd2f1acf1a86c7aeb00aed655e611ad2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc9b0e8438bca2c5d989294321ac3fd033dd901359d03f77e9b545f1ffbdd5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersBrowserTtl]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersBrowserTtl]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersBrowserTtl]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9b571106342a360dccb3b6b33411324990211719353250ef910dba464ce20a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKey",
    jsii_struct_bases=[],
    name_mapping={
        "cache_by_device_type": "cacheByDeviceType",
        "cache_deception_armor": "cacheDeceptionArmor",
        "custom_key": "customKey",
        "ignore_query_strings_order": "ignoreQueryStringsOrder",
    },
)
class RulesetRulesActionParametersCacheKey:
    def __init__(
        self,
        *,
        cache_by_device_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cache_deception_armor: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ignore_query_strings_order: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cache_by_device_type: Cache by device type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_by_device_type Ruleset#cache_by_device_type}
        :param cache_deception_armor: Cache deception armor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_deception_armor Ruleset#cache_deception_armor}
        :param custom_key: custom_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#custom_key Ruleset#custom_key}
        :param ignore_query_strings_order: Ignore query strings order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ignore_query_strings_order Ruleset#ignore_query_strings_order}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5dc4f1f552afa7683d5267005ed7456167729c51d25c824e9fba6195fe1c8b)
            check_type(argname="argument cache_by_device_type", value=cache_by_device_type, expected_type=type_hints["cache_by_device_type"])
            check_type(argname="argument cache_deception_armor", value=cache_deception_armor, expected_type=type_hints["cache_deception_armor"])
            check_type(argname="argument custom_key", value=custom_key, expected_type=type_hints["custom_key"])
            check_type(argname="argument ignore_query_strings_order", value=ignore_query_strings_order, expected_type=type_hints["ignore_query_strings_order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_by_device_type is not None:
            self._values["cache_by_device_type"] = cache_by_device_type
        if cache_deception_armor is not None:
            self._values["cache_deception_armor"] = cache_deception_armor
        if custom_key is not None:
            self._values["custom_key"] = custom_key
        if ignore_query_strings_order is not None:
            self._values["ignore_query_strings_order"] = ignore_query_strings_order

    @builtins.property
    def cache_by_device_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Cache by device type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_by_device_type Ruleset#cache_by_device_type}
        '''
        result = self._values.get("cache_by_device_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cache_deception_armor(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Cache deception armor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cache_deception_armor Ruleset#cache_deception_armor}
        '''
        result = self._values.get("cache_deception_armor")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def custom_key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKey"]]]:
        '''custom_key block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#custom_key Ruleset#custom_key}
        '''
        result = self._values.get("custom_key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKey"]]], result)

    @builtins.property
    def ignore_query_strings_order(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Ignore query strings order.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#ignore_query_strings_order Ruleset#ignore_query_strings_order}
        '''
        result = self._values.get("ignore_query_strings_order")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKey",
    jsii_struct_bases=[],
    name_mapping={
        "cookie": "cookie",
        "header": "header",
        "host": "host",
        "query_string": "queryString",
        "user": "user",
    },
)
class RulesetRulesActionParametersCacheKeyCustomKey:
    def __init__(
        self,
        *,
        cookie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyCookie", typing.Dict[builtins.str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
        host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyHost", typing.Dict[builtins.str, typing.Any]]]]] = None,
        query_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyQueryString", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cookie Ruleset#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#header Ruleset#header}
        :param host: host block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host Ruleset#host}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#query_string Ruleset#query_string}
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#user Ruleset#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41c26b3bbdecd5b59a50b53991c15b99532af58107eb1051d8e0c59a03f3522)
            check_type(argname="argument cookie", value=cookie, expected_type=type_hints["cookie"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cookie is not None:
            self._values["cookie"] = cookie
        if header is not None:
            self._values["header"] = header
        if host is not None:
            self._values["host"] = host
        if query_string is not None:
            self._values["query_string"] = query_string
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def cookie(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyCookie"]]]:
        '''cookie block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#cookie Ruleset#cookie}
        '''
        result = self._values.get("cookie")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyCookie"]]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#header Ruleset#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyHeader"]]], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyHost"]]]:
        '''host block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host Ruleset#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyHost"]]], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]]]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#query_string Ruleset#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]]], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#user Ruleset#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyUser"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyCookie",
    jsii_struct_bases=[],
    name_mapping={"check_presence": "checkPresence", "include": "include"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyCookie:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of cookies to check for presence in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#check_presence Ruleset#check_presence}
        :param include: List of cookies to include in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21036ad820adc9ecf2e54a6139026c938822ca8e16635180e68513d64e53112)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookies to check for presence in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#check_presence Ruleset#check_presence}
        '''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookies to include in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyCookieList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyCookieList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93de0251987de35689d65ce443ab2228387dcc80ccaf02e035d186ecfcb092db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ac471c888453e2194de3aba8a0fdb92e23ad58ae3df815bc86de7fa440fc0d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e9c409a3aea876f100fdf3403f0f65469a8f16abf33cbc04c4b71e2357565f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a17a44eceef8425038bf92c6a51312963d62100bfd3c96ef4eb6881404716359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86cc45083e22dd050bc9bfcc5d916d3eedda93c2f59323593a86055cdd95847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1baab91a494f0d69418d90eb8f2d036330211ca0e9eb66e68184dd38d498c974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cb0d96812e9e5dae46a3ca32ff3e21bc820473d8f677e46d83049000c4219f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf3ffe785d78da5a3110b29424cfd439b8bfa9df5c34c242be2fd4cd4e95dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537ff1156b88f89b7234398ff7bb2b3f14709a2266eb67cf78c0fe596db42d18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyCookie]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyCookie]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyCookie]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7720c5dab1bff1d3bc87be21df59916d787fad17806baa9a624aca8b24dfee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHeader",
    jsii_struct_bases=[],
    name_mapping={
        "check_presence": "checkPresence",
        "contains": "contains",
        "exclude_origin": "excludeOrigin",
        "include": "include",
    },
)
class RulesetRulesActionParametersCacheKeyCustomKeyHeader:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        contains: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
        exclude_origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of headers to check for presence in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#check_presence Ruleset#check_presence}
        :param contains: Dictionary of headers mapping to lists of values to check for presence in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#contains Ruleset#contains}
        :param exclude_origin: Exclude the origin header from the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exclude_origin Ruleset#exclude_origin}
        :param include: List of headers to include in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5736cf4f272699136c8f912f9c796dd3759d9bceacaf833672b0b527a785e9d)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument contains", value=contains, expected_type=type_hints["contains"])
            check_type(argname="argument exclude_origin", value=exclude_origin, expected_type=type_hints["exclude_origin"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if contains is not None:
            self._values["contains"] = contains
        if exclude_origin is not None:
            self._values["exclude_origin"] = exclude_origin
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of headers to check for presence in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#check_presence Ruleset#check_presence}
        '''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def contains(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]]]:
        '''Dictionary of headers mapping to lists of values to check for presence in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#contains Ruleset#contains}
        '''
        result = self._values.get("contains")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]]], result)

    @builtins.property
    def exclude_origin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Exclude the origin header from the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exclude_origin Ruleset#exclude_origin}
        '''
        result = self._values.get("exclude_origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of headers to include in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHeaderList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe13ae59c7bded6757aae25a012e8e7ba0787c156461c3e346e0cf246fa46819)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83ee8de63ae449216f78872986cb87635781b8cfdb65b3a1ac8914058026c7d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25707e45d5604174906e739421cfb03d5b3a86ca7c37b73190d98b93ab16e528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85feea8dcee35eab665cce2f4914c1c2f77ead9e2268f3fe3b22c46fca8763b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d07ad3fbd9415a2aee0aace1a5fd85b5a820341eed5335cd3aded196da3ab7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e64d7b56a3bf46b8eedfcb9f889c66189e8fee40f101c7c1aba3ee8ef2e1d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572c1c886983afb6c5088c782e9999218d206f6c94de79704997c04a20798b49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetContains")
    def reset_contains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContains", []))

    @jsii.member(jsii_name="resetExcludeOrigin")
    def reset_exclude_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeOrigin", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="containsInput")
    def contains_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]]], jsii.get(self, "containsInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeOriginInput")
    def exclude_origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "excludeOriginInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f76d37c74d0200150e44a0d00a759e21a645b9da99f2200fb5ed676750ef0ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contains")
    def contains(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]], jsii.get(self, "contains"))

    @contains.setter
    def contains(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c63441fad8ce42badc7990b9d3d2921ad2e1947861d8ea2f6f72fb1407dbc514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contains", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="excludeOrigin")
    def exclude_origin(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "excludeOrigin"))

    @exclude_origin.setter
    def exclude_origin(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__099d77f63dcc5d9e03581c4ea12ad3e4df8c15e0d705c49e3cf2159fb950fb13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeOrigin", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c038ed08b946ce1ba9d3cd8c177d1d5712953b5613bbb02f22e5e3ed46e0c3e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHeader]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHeader]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHeader]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c561e0ed3436a5035fef2a0947bf09385708368c401ba65b2aa395b05326e884)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHost",
    jsii_struct_bases=[],
    name_mapping={"resolved": "resolved"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyHost:
    def __init__(
        self,
        *,
        resolved: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param resolved: Resolve hostname to IP address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#resolved Ruleset#resolved}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172655455e537081c566b2ab3b5a9e353c1b3ffcc4ac8f47dd43e22a2026ec15)
            check_type(argname="argument resolved", value=resolved, expected_type=type_hints["resolved"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resolved is not None:
            self._values["resolved"] = resolved

    @builtins.property
    def resolved(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Resolve hostname to IP address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#resolved Ruleset#resolved}
        '''
        result = self._values.get("resolved")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyHostList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHostList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910cf0aecfc13fef55616c107dcb604bb99e0f8ac49067ba2df9fcbb0c4fc1af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13244f99723fb749545930598af63110908b9b6ab2e222b19b6d0420880c0e6b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa37648d04bc631e00f0abfa176554dfde489c03ad80352b449c6eb4a253553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d193fb023323a8e8c02d6e91151c6a439a1326654aa27da466230b8b22d182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9140cc7eeb6ce4732ed3dcc2150f4de68cc71620e02da38bb3e726559f2b229)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfacb13d0c4ae8de37219e62e4da6bbc0099b163e8b0a650a83fa5663c07c29f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cab141b386661b5f82059c12be685445b2c72626547bbd0a6e335ea2a2042cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetResolved")
    def reset_resolved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolved", []))

    @builtins.property
    @jsii.member(jsii_name="resolvedInput")
    def resolved_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "resolvedInput"))

    @builtins.property
    @jsii.member(jsii_name="resolved")
    def resolved(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "resolved"))

    @resolved.setter
    def resolved(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b21686a047e96b688dd7e438de047c689a9bcb443e2535de17dc5039d4d1247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolved", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHost]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHost]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHost]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1206431d417cd671814597583ac30781b1d4c12674b8ce0756268127ad087011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f20eeb11f492c38f80070899ea81529d2c83f8ad1a82f716007068b15c2437)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1dcc286802fb640ce3de13e3eea795a849c11e263219572b7033aab6db432ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16999b302d6a4530dad1116969d675d022b6eaf8bb4faa249b84f7546599904f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68a85f4c3bc632ff6f6b50a349e68968e919c7e92434ddafddd4353ea645cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8d6c5fec5d15090a0c66ab1461c5f40aac2a8876159e99e3b07ec6ad6151ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa3c96ccc2f11908575a9d6318744e897fac20bb51a4ec90985d3c79bc6547b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3e9c0d9998ae16667369b9969dbb9669968802cedb705b719a998fcc8e7e25)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCookie")
    def put_cookie(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyCookie, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac138deeb48fa0d5738e9c6fa9b11d51b6411ed75951dfaf0a28680c9ffac9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCookie", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f761fd3d74609ee17cf205b3d46e784975328cec019a7a574a3ec77fff459c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHost, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a8287ef153780193a8eb807894afeb92bc77579645952d407b021cb0ea1a64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyQueryString", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e968a38de883b5388e3e4364c01639f6ade5ecc7210c3ce8188b8fbf737141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd7a4858c06821c37ced77eb072525c4457cb2434985ed0aa909fee3b8a953e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="resetCookie")
    def reset_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookie", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="cookie")
    def cookie(self) -> RulesetRulesActionParametersCacheKeyCustomKeyCookieList:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyCookieList, jsii.get(self, "cookie"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> RulesetRulesActionParametersCacheKeyCustomKeyHeaderList:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> RulesetRulesActionParametersCacheKeyCustomKeyHostList:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyHostList, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringList":
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyQueryStringList", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "RulesetRulesActionParametersCacheKeyCustomKeyUserList":
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="cookieInput")
    def cookie_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]], jsii.get(self, "cookieInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersCacheKeyCustomKeyUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKey]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKey]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKey]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea3644371990a184e17695faceb338d641678396fcfe966d9e151a71a233215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyQueryString",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "include": "include"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyQueryString:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: List of query string parameters to exclude from the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exclude Ruleset#exclude}
        :param include: List of query string parameters to include in the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7b4285fd61de06c6ee33a490a292729c0bbe60c2c265b6db5eea8da223f67a)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of query string parameters to exclude from the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#exclude Ruleset#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of query string parameters to include in the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyQueryStringList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyQueryStringList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2f2558eadf7ebeb6d1f261a53174043fe5ae00eb5e4cf36430fc56090620b83)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dac35c4dce316f9795d8cce8485dfbfe163e0646f4ddfd83a2c18f9d340dfd0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad34e64a2cf2bbf940aade76f3b3bcdbbf2604b15470670c70cc62b4bb641e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef93d9259b21a757be5b299cd07c0d3167151e131e5fd5b5ae792c2f45c2da2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5cf6a58f0b4358533b719030ba3787d21d71964fa5a2274fb9decae188e82f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyQueryString]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyQueryString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyQueryString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3371c5b4ed76dab28a448c4b961601796d3f9d89e3c74541b2bb0e0e0a5bd11d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3c93b34094c2b75e4b99f9670bad451c73e6bbd510673419efbdf0395ee4e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0da3a55291f064fdb5faba25fa71b0b7fe575dfeb35315939174070bc5a0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f683aa3c6de4602169f3a050011d700e570eed5446d978bf4d156bb97984e4d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyQueryString]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyQueryString]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyQueryString]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df7aac92d496eb8e393664433b150825479f1ab67fcbb375b8b2b06f786b3fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyUser",
    jsii_struct_bases=[],
    name_mapping={"device_type": "deviceType", "geo": "geo", "lang": "lang"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyUser:
    def __init__(
        self,
        *,
        device_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        geo: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        lang: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param device_type: Add device type to the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#device_type Ruleset#device_type}
        :param geo: Add geo data to the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#geo Ruleset#geo}
        :param lang: Add language data to the custom key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#lang Ruleset#lang}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e924452562758bc0029e3f097ee591730962722f9415cbdae62ad5c99312a6)
            check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument lang", value=lang, expected_type=type_hints["lang"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if device_type is not None:
            self._values["device_type"] = device_type
        if geo is not None:
            self._values["geo"] = geo
        if lang is not None:
            self._values["lang"] = lang

    @builtins.property
    def device_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Add device type to the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#device_type Ruleset#device_type}
        '''
        result = self._values.get("device_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def geo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Add geo data to the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#geo Ruleset#geo}
        '''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def lang(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Add language data to the custom key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#lang Ruleset#lang}
        '''
        result = self._values.get("lang")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyUserList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593689f789b8f6b8a98b7268ef71cef873aa5f9137fc7e1e575e1ab408c025b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8470744f3b156a3a8f8e42851b8c735f204cdd3d5b2a33874a1d6514d25af3e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__875dbc081643c98f7cd387df5f4d886ce4954f694bea37b1a257cefdc7b744b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b33560c1b67f255789ca6b7bf80e494ac4991128764dd23dc199b491deee05d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2120e46eb10538e254daaa06cc920c52c779db84abc9c971bda3db666a7f60a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c830910c74b026710062a65e2197b789478c76f820d0f335917460b90b1d8a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54755d8b6a77713d1f599449b00c107d0606ce8da84a3089e41ea527a32979f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeviceType")
    def reset_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceType", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetLang")
    def reset_lang(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLang", []))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeInput")
    def device_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="langInput")
    def lang_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "langInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceType")
    def device_type(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deviceType"))

    @device_type.setter
    def device_type(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__118e87128a54c0a6a808884398111aa7d7e42619ac2998ed9c7994149a2e673c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "geo"))

    @geo.setter
    def geo(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ec499284751ea78350e508a3abcbcb5d358f36ea55633d83cd7544ecfcd8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lang")
    def lang(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "lang"))

    @lang.setter
    def lang(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__649cabf797e6afb01eb8f703947d9cfd1d2f6e8e6124fa69fce18fc09c189c90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lang", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9927298f8b3d3447fe8f48459da6d6a83934967c742bb540bf20da76127120a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b01ba3453b6c20ef499fced682b50f9740f78c2596db43329ac5b81996672c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e50a4885609bc6b6e71c8fa3b69fe38530df6d19d3d40bd025dc6eb10f548b17)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c5c89fa17d8ea711f302e0fd81dc9d4c066942a9a00d6e00356a7e288a714b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c5943ef13104c0a358cf5fb7fc13c3f07b65c0931de99c118984b8fc048836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc93b2a9d8f6c6ebc157d2d06e31278aa114c6b44527772d47a1857ffe70cd7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772e60af4421c33a856fdd865196555f4058c09ca10a6a020405ad4c82d42153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b8429f9631c7f4e81e16a71bc7d2ba9e3a4a61fec48eeea0f1e6eff39efd34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomKey")
    def put_custom_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKey, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cdfdbf8a49fcc502d1c98a4ecc2eac53348f32515527b9e9b76e44a9f7a0cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomKey", [value]))

    @jsii.member(jsii_name="resetCacheByDeviceType")
    def reset_cache_by_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheByDeviceType", []))

    @jsii.member(jsii_name="resetCacheDeceptionArmor")
    def reset_cache_deception_armor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheDeceptionArmor", []))

    @jsii.member(jsii_name="resetCustomKey")
    def reset_custom_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomKey", []))

    @jsii.member(jsii_name="resetIgnoreQueryStringsOrder")
    def reset_ignore_query_strings_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreQueryStringsOrder", []))

    @builtins.property
    @jsii.member(jsii_name="customKey")
    def custom_key(self) -> RulesetRulesActionParametersCacheKeyCustomKeyList:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyList, jsii.get(self, "customKey"))

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceTypeInput")
    def cache_by_device_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cacheByDeviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmorInput")
    def cache_deception_armor_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cacheDeceptionArmorInput"))

    @builtins.property
    @jsii.member(jsii_name="customKeyInput")
    def custom_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]], jsii.get(self, "customKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreQueryStringsOrderInput")
    def ignore_query_strings_order_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ignoreQueryStringsOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceType")
    def cache_by_device_type(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cacheByDeviceType"))

    @cache_by_device_type.setter
    def cache_by_device_type(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7008c0f9237f3579ed64d4615be741d342fa0810924e2ab328fdfc511bea72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheByDeviceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmor")
    def cache_deception_armor(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cacheDeceptionArmor"))

    @cache_deception_armor.setter
    def cache_deception_armor(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cbc18ad859c2e5194b72377e26f9d1168619a5982b43b3364bc18606b92f870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDeceptionArmor", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ignoreQueryStringsOrder")
    def ignore_query_strings_order(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ignoreQueryStringsOrder"))

    @ignore_query_strings_order.setter
    def ignore_query_strings_order(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d70ccbb43451c8e3713800708a04ab330bfdac22e4e81e3ff7f152a6ad9077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreQueryStringsOrder", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKey]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKey]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKey]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5e95b07849f4be277ce84da62fec0c34d592a229699ce2c8ff002136fac1e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheReserve",
    jsii_struct_bases=[],
    name_mapping={"eligible": "eligible", "minimum_file_size": "minimumFileSize"},
)
class RulesetRulesActionParametersCacheReserve:
    def __init__(
        self,
        *,
        eligible: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        minimum_file_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param eligible: Determines whether Cloudflare will write the eligible resource to cache reserve. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#eligible Ruleset#eligible}
        :param minimum_file_size: The minimum file size, in bytes, eligible for storage in cache reserve. If omitted and "eligible" is true, Cloudflare will use 0 bytes by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#minimum_file_size Ruleset#minimum_file_size}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb239771d4009aed0c39f9f48bbed27aa2d69cfe4ad90ba4e2f0f2edf518b2a3)
            check_type(argname="argument eligible", value=eligible, expected_type=type_hints["eligible"])
            check_type(argname="argument minimum_file_size", value=minimum_file_size, expected_type=type_hints["minimum_file_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "eligible": eligible,
        }
        if minimum_file_size is not None:
            self._values["minimum_file_size"] = minimum_file_size

    @builtins.property
    def eligible(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Determines whether Cloudflare will write the eligible resource to cache reserve.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#eligible Ruleset#eligible}
        '''
        result = self._values.get("eligible")
        assert result is not None, "Required property 'eligible' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def minimum_file_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum file size, in bytes, eligible for storage in cache reserve.

        If omitted and "eligible" is true, Cloudflare will use 0 bytes by default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#minimum_file_size Ruleset#minimum_file_size}
        '''
        result = self._values.get("minimum_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheReserve(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheReserveList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheReserveList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8445055a29da7a38852fa1ab9b21c675888a8c6e8c9b571b8ff055058241c699)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersCacheReserveOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cce0377fbcad472143a3a282d94881af9fabe86e9d06dc4189de62a12b4de4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersCacheReserveOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48271d120498cf0035319f9841b704a6711ed031daaac1f0a19f3f56fd1f3e21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77aec4e48ff9ce8f9ba2735a335684e837764aa4c0b8a84f641fe76fc7b6e6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af703b933f54dcf6e920e7116f0191bdd7cc48baf923706e41c70bc79300408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd07171c652766038cc4a10e92ad7d04390bbbfdb33ba8f9346a5c819973b5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersCacheReserveOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheReserveOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83846cb6c021d54cae085d576ebf881b257d4710c2a21c7bbf1cb2a863df2730)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMinimumFileSize")
    def reset_minimum_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumFileSize", []))

    @builtins.property
    @jsii.member(jsii_name="eligibleInput")
    def eligible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "eligibleInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumFileSizeInput")
    def minimum_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="eligible")
    def eligible(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "eligible"))

    @eligible.setter
    def eligible(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50fc546e11eb198d4c672f0e18d9634f12bfb8b1f8e5af296aaf0cd779374723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eligible", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minimumFileSize")
    def minimum_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumFileSize"))

    @minimum_file_size.setter
    def minimum_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2393a403b9e110ef3fe0dc538beebabf227c07e9e5a4c04b1a1ed6cd664c9769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumFileSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheReserve]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheReserve]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheReserve]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c172960cf40cacaf939cd31c3e19373dad237d9be2d4abc42711c8d2ef26f55d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtl",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "default": "default",
        "status_code_ttl": "statusCodeTtl",
    },
)
class RulesetRulesActionParametersEdgeTtl:
    def __init__(
        self,
        *,
        mode: builtins.str,
        default: typing.Optional[jsii.Number] = None,
        status_code_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtl", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param mode: Mode of the edge TTL. Available values: ``override_origin``, ``respect_origin``, ``bypass_by_default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mode Ruleset#mode}
        :param default: Default edge TTL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#default Ruleset#default}
        :param status_code_ttl: status_code_ttl block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code_ttl Ruleset#status_code_ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2adbcf077256eea528469fe51105b233df404214ccaeca6a85e07946e6a0d1a)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument status_code_ttl", value=status_code_ttl, expected_type=type_hints["status_code_ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
        }
        if default is not None:
            self._values["default"] = default
        if status_code_ttl is not None:
            self._values["status_code_ttl"] = status_code_ttl

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode of the edge TTL. Available values: ``override_origin``, ``respect_origin``, ``bypass_by_default``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mode Ruleset#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[jsii.Number]:
        '''Default edge TTL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#default Ruleset#default}
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status_code_ttl(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]]:
        '''status_code_ttl block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code_ttl Ruleset#status_code_ttl}
        '''
        result = self._values.get("status_code_ttl")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e99dabe5822010205510f1e95095bc12a24e3eda5939ae518b0ad06a1f1433e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersEdgeTtlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f67a9aae03da6be6f4fa39595fe245c806fe408cacccb946c75436bb94d1b5a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersEdgeTtlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d43ee02c025cec0da804e9254c0fb5ffe8d78978e2bcc389e05069a8c3c8ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c940e258b9eecdd8954a0938ebb7d5edc937a78624d8599ddd0789268000a970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb5305398f8126a5dfdce28e14789079305ed85b4d805bee88c58482ba1bc39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753b5b7f30b1fdfd74881fd6768da28679557a329a222c0d42729fd9b4e2491a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersEdgeTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d26af6f6e3836ca45f2f660b7f6fc6e440a5708bc24173a2f9a9b93e521909)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStatusCodeTtl")
    def put_status_code_ttl(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtl", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5898aed30519c65916f3516e03b0c5b2a482618fbb99ff8eed8692e10109f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCodeTtl", [value]))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetStatusCodeTtl")
    def reset_status_code_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCodeTtl", []))

    @builtins.property
    @jsii.member(jsii_name="statusCodeTtl")
    def status_code_ttl(self) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlList":
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlList", jsii.get(self, "statusCodeTtl"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeTtlInput")
    def status_code_ttl_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]], jsii.get(self, "statusCodeTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "default"))

    @default.setter
    def default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca1b9a6f1a714476b55bd9b153038e933b01ae1e9de408b86c1bf1638079064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d4345630e346df22f1e89d154dde919e4502eebb8e88265688414f0a2626cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtl]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtl]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtl]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2050d59e7b65ed514e7e5062fc10e07e175a5a72a4a676658d4a61742216c145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtl",
    jsii_struct_bases=[],
    name_mapping={
        "status_code": "statusCode",
        "status_code_range": "statusCodeRange",
        "value": "value",
    },
)
class RulesetRulesActionParametersEdgeTtlStatusCodeTtl:
    def __init__(
        self,
        *,
        status_code: typing.Optional[jsii.Number] = None,
        status_code_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param status_code: Status code for which the edge TTL is applied. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        :param status_code_range: status_code_range block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code_range Ruleset#status_code_range}
        :param value: Status code edge TTL value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3673fa2048e013a4a46d6ac26004801528dda62f81db6c2fa68f68e01e0e6605)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument status_code_range", value=status_code_range, expected_type=type_hints["status_code_range"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status_code is not None:
            self._values["status_code"] = status_code
        if status_code_range is not None:
            self._values["status_code_range"] = status_code_range
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Status code for which the edge TTL is applied.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status_code_range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]]:
        '''status_code_range block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code_range Ruleset#status_code_range}
        '''
        result = self._values.get("status_code_range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Status code edge TTL value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtlStatusCodeTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba6f59140aebf5b4e01a4909e04a155d21689935bed3a5bf7fe8bf2cb172c6de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5843232fdc4262447b546bd8656f2b9ed6644c356c348f236ce488e742c19422)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__097d1b4ef1a297f0eefb68f409edb861d1a8cde46543feda4611b83b979b8424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c81f7217d11e61fc2a9db0de37ad26efa084c3f3cd7f47d464d5c57af1996b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4610355139bcea4c6748dcb306da92e33ad66b1f47ac0bbab3f8917d72ae58c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37eeb71739e6dd95fbedb9551cf3217e66c0e88fcf675c98f35c89376a6a3de5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08afdb74723920f7da0de5c614b150aa3088a3701db265eca5a162a255a9a98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStatusCodeRange")
    def put_status_code_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5243b09455914f0120eb29dd6eb000de5bf20fc7a9d63f3fb5d478a1481c818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCodeRange", [value]))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetStatusCodeRange")
    def reset_status_code_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCodeRange", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRange")
    def status_code_range(
        self,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList":
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList", jsii.get(self, "statusCodeRange"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRangeInput")
    def status_code_range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]], jsii.get(self, "statusCodeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980ec2945afc28a2effc73cc55fc03e92f12feb6ec75e13e6a35fc6420b210cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b95217c7f7c8ad8bc9127cbd39ad24b346025d33d55d6c1133a144242062ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtl]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtl]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63905ff61e4ef02f2c86e426d9de5bcee56988e80e3cb5c2fd68cdb775f2e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange:
    def __init__(
        self,
        *,
        from_: typing.Optional[jsii.Number] = None,
        to: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param from_: From status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from Ruleset#from}
        :param to: To status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#to Ruleset#to}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4a25235665711c4041ce37b303e51598ad26898a434cc3160e4917eecb8ef7b)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[jsii.Number]:
        '''From status code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#from Ruleset#from}
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def to(self) -> typing.Optional[jsii.Number]:
        '''To status code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#to Ruleset#to}
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__040a8a88ebb01a29492392c17126b54eea1ea94afc74ff97913ce0dbdf294767)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9472aa688b2900ff5dbd9336e12ac006c9f95fb4c2cf7e8419663ace930474df)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6154090fcb398a6c323daac743800e63ca2d2a8fbf1eb9a6b5a66302ae83abac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f40a2d416012b5cfdf4b7020fa1687c80ed9a93f86666057e51b59b23dee7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__743c87b95a0b9c57cffd8871e4d5a803027bfeeb5e1e77479066bfea4e7e2529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee21671353a5b3b96ac92ad182d8a08ac585883230482b75b76a0b170ba008e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc2e4b4c701b4f62c3d3e1af53d1d6346d822b38d7e7ac1cd0fa012491fc944)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetTo")
    def reset_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTo", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="toInput")
    def to_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e3afbf86ba5f2b22b890fb6422ab6bb7a12c012c2415abf31ae2ca5e246fa6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @to.setter
    def to(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1698a22751a5220477692ed03bb293b1cfa2534c0e9729f13df8b09be13c2bb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "to", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ccd858829d1059e0b6f536c3fb04871be3b7ca1dadb6167ed1b45eca02a7efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromListStruct",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name"},
)
class RulesetRulesActionParametersFromListStruct:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Expression to use for the list lookup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#key Ruleset#key}
        :param name: Name of the list. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b67297e45830ba9e9e493dc7bfae4e3f7f64c4196d83dfe3bfcc5bb28b4b507)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Expression to use for the list lookup.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#key Ruleset#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the list.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromListStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromListStructList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromListStructList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c70b4dedaa910db647d1f9addebc1e5dd138003a9112dda81235689081d26d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersFromListStructOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ebaeb0283c3ee7b7722699a88fc3db518690e353bee97bfff8abd3e39bed2c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersFromListStructOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c308d650bd04f850182eaadb8efe3a78c86d53860da0bfcdfb3338663a91b824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c800838c4e46849d084c83e3b2de1ac0e1230488ef3532ee6f3702154fdc28ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a05634e13bf31c84ce334ee20506c2dabbf15a48ddfd3003480eef2bdeac5d02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da4f3a9a1e2ec52a5bf1492801389733065b3a643724ab55363f66c2f60337c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersFromListStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromListStructOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ad50478c51ebfe851a1202f0eee561e58ac9c8d5ac9f9dd845445be7d27095)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc57cee4e4d328d61e69700340a43b873375e6fd941a218084660ea69230e2e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904a219d759fb3dd4fbb6cbdaf10fde17cd05747e9712f93eb196ba2d494fcdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromListStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromListStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromListStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e569509f78948c3b20e7351605121e529c164557e790879d1bfc357deb39ef1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValue",
    jsii_struct_bases=[],
    name_mapping={
        "preserve_query_string": "preserveQueryString",
        "status_code": "statusCode",
        "target_url": "targetUrl",
    },
)
class RulesetRulesActionParametersFromValue:
    def __init__(
        self,
        *,
        preserve_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        status_code: typing.Optional[jsii.Number] = None,
        target_url: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersFromValueTargetUrl", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param preserve_query_string: Preserve query string for redirect URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#preserve_query_string Ruleset#preserve_query_string}
        :param status_code: Status code for redirect. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        :param target_url: target_url block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#target_url Ruleset#target_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b617685cddbd9ff58e47258970e6023730c625e0d17d160b4bc521fea77e88)
            check_type(argname="argument preserve_query_string", value=preserve_query_string, expected_type=type_hints["preserve_query_string"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preserve_query_string is not None:
            self._values["preserve_query_string"] = preserve_query_string
        if status_code is not None:
            self._values["status_code"] = status_code
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def preserve_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Preserve query string for redirect URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#preserve_query_string Ruleset#preserve_query_string}
        '''
        result = self._values.get("preserve_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Status code for redirect.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_url(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValueTargetUrl"]]]:
        '''target_url block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#target_url Ruleset#target_url}
        '''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValueTargetUrl"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30bef636aae2dd330b55ce293888f5e6ce57e738acc7f9d74f824ec974c2e65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersFromValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25a97d48e0beb53f6e5943adad5e01abe957af29ba3b866ce81dfb0cedc41b3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersFromValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6173b7480ff7497bcb2b857b117b8f18ba74f6388a18a790aa194fd00399235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80fc1c8b77efe450d39b59e8ee2351e201384a7c902fe2f7e7ff31009a1d3f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b71064ce6fb285eb20bb40e5a41e5bb973813ec288900eb962921e1ca2fa04ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c35341bbc5554ba31bf595eab6a01b1b4157e05a74c3f1b5570bc23d9afde2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersFromValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14bfcc9e7facb7af52daa289700b5fc68804c2bb13e920e75cea840d3b11b0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTargetUrl")
    def put_target_url(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersFromValueTargetUrl", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14e09462c0a00668ad50264267e33e4c499985a1a05c944d58291f14d842027b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetUrl", [value]))

    @jsii.member(jsii_name="resetPreserveQueryString")
    def reset_preserve_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveQueryString", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> "RulesetRulesActionParametersFromValueTargetUrlList":
        return typing.cast("RulesetRulesActionParametersFromValueTargetUrlList", jsii.get(self, "targetUrl"))

    @builtins.property
    @jsii.member(jsii_name="preserveQueryStringInput")
    def preserve_query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preserveQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValueTargetUrl"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersFromValueTargetUrl"]]], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveQueryString")
    def preserve_query_string(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preserveQueryString"))

    @preserve_query_string.setter
    def preserve_query_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442bab0415161d2c44f7b4a8f57cc53c0ebb063a2d7ca08364042c29a4896e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveQueryString", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c246ee97ca8b910ef616470f8d160ef0d00fd420db6b68d517088664670d6026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eb247ab659e2fbaf89fa2a257186f1bec68b5cf2c6fa4761bd9d050c347c2a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueTargetUrl",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersFromValueTargetUrl:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        :param value: Static value to provide as the HTTP request header value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02bd6ce7e2bfcb866a45913cbaf053071a80f5319b55ca46771f3e7db50fd167)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static value to provide as the HTTP request header value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromValueTargetUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromValueTargetUrlList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueTargetUrlList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28bfd24702742ec150e14e6094196d9f8c8eeb0aaa14efe9d6645c0b9a0b4168)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersFromValueTargetUrlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57772fddb4ba4abfce84fdc378cf1f3abf373ee1c9579255611b9eacbb4d23e1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersFromValueTargetUrlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d7dc57ee3086bf96292c9ccbe19be26a3c74699c1cfac682272f72ee92dc9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__719ce08bdd959f10cbff26c8414ab42d1b464d0885667531a55e12fe0010c5fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a6d878e0bc78932ff50d7a062152eb88bda71a79893f5f88e5a0942d24ae1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValueTargetUrl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValueTargetUrl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValueTargetUrl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9296ed72de38c1dbb3a7cba9fe44e54d0445e26c2a2683f5814275259427657e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersFromValueTargetUrlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueTargetUrlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c4252337abab2e0099a3ad31e7175f65f58f06fb6590b6f9f8553cec9345fd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4534868c475de22c561632b0d8e024ebb69e1aa7725e25fda4a979228e80457e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41518c81dc91a8969ddd1b9af70402b5dc007c626f7b933766f981c088a0a86c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValueTargetUrl]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValueTargetUrl]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValueTargetUrl]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913ba6418e4bc925f63b590b04b1a7cb716e01f738a10685f09bf63982b2e7c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "name": "name",
        "operation": "operation",
        "value": "value",
    },
)
class RulesetRulesActionParametersHeaders:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        :param name: Name of the HTTP request header to target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        :param operation: Action to perform on the HTTP request header. Available values: ``remove``, ``set``, ``add``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#operation Ruleset#operation}
        :param value: Static value to provide as the HTTP request header value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9652b0b730f90edd91411f20b54239e14e14ff06dfc563f9f61e3a16b6c048)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if name is not None:
            self._values["name"] = name
        if operation is not None:
            self._values["operation"] = operation
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the HTTP request header to target.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Action to perform on the HTTP request header. Available values: ``remove``, ``set``, ``add``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#operation Ruleset#operation}
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static value to provide as the HTTP request header value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersHeadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeadersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b8d4da10e304c7f89199d5211474b4c651342e5f5b9ff3803b37c9b64c5d1ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__299fcca6fe4873c00ab6794bb6b10aad87b575f6f9d9b2f50391cb1101792070)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc9531dedfa7905814b7cb90d7299d5ea25a1c2ebc8041d021398ae2694711f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__064db88945a642179712db631f02bd779d5a3340a7f89784a34c155fa6448ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba7b0ed17ce15bfbcf785f2a71c7fe4a6bae38e9e5c056578a79043bc965b78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939291c9079aaaff2564e65706c33760d7f74110dc6497567e42d9f73d6c256a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeadersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfacdf328fa2609ecd011de17a875188c7bafaa8bb1b8105e15fef25add34b1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d822d3d4435667164f8ded41e86d5eaf60d62b7a7eaf88bb32cc1a577611a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b108ca26ef5770c015de28b30b6426eb37c44a2d0d33fe7939b38605852f9da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2588ff959f1b47df89bd43164ac4a93c851c4b6f618800d15502e7e671335444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840a8ae1386a674b2471be5f3aedcd3c8d7b05284c75ac7ca593dca0dbf1b571)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersHeaders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersHeaders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersHeaders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8dab90cc37dec2cb13251cba8532102fa4c230c824aa25858ba19a577652c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4fab722cfa46a0a5e696b2d315e34e0439cbee15d40d884fb6d5c3fe8f92d78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RulesetRulesActionParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726e7e6036ce6403a84e26955581dda67b111f473ba057ad31fdb4690421e961)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e012258b38d9ae121b559d84c7d1e4c1bd1c7386ca404b508e29e5395a2d3a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed3b9146080004d928c3a56b95c0ed6d737078fcd652a66cb2dc27c11159654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6849de5e327a7c1c88bbec20248113c141eba97b65c5e518eb5b395eea1986e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8534cb92b7abffe1e93fc9c65e1cc98a2d21d6b8954eebd036e5060fed87defb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersMatchedData",
    jsii_struct_bases=[],
    name_mapping={"public_key": "publicKey"},
)
class RulesetRulesActionParametersMatchedData:
    def __init__(self, *, public_key: typing.Optional[builtins.str] = None) -> None:
        '''
        :param public_key: Public key to use within WAF Ruleset payload logging to view the HTTP request parameters. You can generate a public key `using the ``matched-data-cli`` command-line tool <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/command-line/generate-key-pair>`_ or `in the Cloudflare dashboard <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/configure>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#public_key Ruleset#public_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79d24480fd9fa655d9e35cea6778e368ef22b575957402a26c1ce56e67b78a5)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''Public key to use within WAF Ruleset payload logging to view the HTTP request parameters.

        You can generate a public key `using the ``matched-data-cli`` command-line tool <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/command-line/generate-key-pair>`_ or `in the Cloudflare dashboard <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/configure>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#public_key Ruleset#public_key}
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersMatchedData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersMatchedDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersMatchedDataList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eca00da8071730d4011489c64266d9884fe24abbfd6607ac3d2ed01a5e2fa41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersMatchedDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7684b7762ac064774bb2f9c1631432728a80d08f58ed73bde541cf6631c34d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersMatchedDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15620bc3c76dd25262a3a05bb5455de97bb3349809ee6f28ebc6e9a87a009fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9d1a56694297e6b933d8a166933a5b9dcf26690f65f67b97a4cfeb13fa20fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83e0a5be466a7b77fc0fb78fd725b1a5f6e6a45a232a8a69f81d7f5b1ac7013a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ce39b0c59daf679cd7a1964f516c86a8a616a9db99975b8d908233b9338ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersMatchedDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersMatchedDataOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba186a9743494693779a9e41dd6a2b9d0a4a06edd39331ca226b8a283c9fc29d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPublicKey")
    def reset_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKey", []))

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeeae244ab63610c3b8e2d8d04684195e4c143626b564aaa8ad018a99b99077e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersMatchedData]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersMatchedData]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersMatchedData]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10459137af99ae34d414b273da7570a083799c03706021cc90528bb03dd4622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOrigin",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class RulesetRulesActionParametersOrigin:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host: Origin Hostname where request is sent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host Ruleset#host}
        :param port: Origin Port where request is sent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#port Ruleset#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__538f5da67f00eda4fe4eee29f992b9343c58a3da7e13f4f9a7eb2b45e7640f08)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Origin Hostname where request is sent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#host Ruleset#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Origin Port where request is sent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#port Ruleset#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOrigin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOriginList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOriginList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22510ec03ab1a4f34b5555e2f261bf7d62afd66106a6a83c84edc02c03422bfd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOriginOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35350591ea0d047cb4f14172a81482f1ba021ca9b985fbd2fb49265363a2e2ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOriginOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e72d426ebf637376a4f9a0306d8bf9350699137481684dc89132ef3fffdb87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439ca7ca3ad95ea1669474aa7555437678d1c4d4c77f652bd3c2d7195b6c2481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41af885442abf9b95872c496b45047e70b7ffabfb92ed680f0c46f4aabf9170f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc110626641facc7ed95637134bee238f59c36f873b09913b771b723eb4ec725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOriginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOriginOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4834ab77b72906e58302c5d50fd0a4eca483b2ba55ab4149ca7bea453e1fd4a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146fcfc00aa700c091a6ff77222191f183182f60cc02c42931892d61288ec6c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7298adec8969ec5c380dd8fce19252739063f1d26ad76f4ab92c9c406edbf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOrigin]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOrigin]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOrigin]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa92555cb9bd54c4a1adb3c18197cc7867b725494398451bf2f4a58d125f7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27dba44e1ea75e7aad0490ea79a278b382f6f2d89f9e284e704a7d57ff8ef774)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAlgorithms")
    def put_algorithms(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAlgorithms, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a20ca357c17361d0dcbe282dae4126a3d1ff2dca9643447637f85a4a2ede9e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlgorithms", [value]))

    @jsii.member(jsii_name="putAutominify")
    def put_autominify(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAutominify, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad0ec3e765a1241cf39527fcaca381777a6ee8fab3cffc68d06214b5df97cb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutominify", [value]))

    @jsii.member(jsii_name="putBrowserTtl")
    def put_browser_ttl(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersBrowserTtl, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3113fbc38cf58a3a15fc8c4132ab3fe8544adbb924cff02904a6e12952e50dd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBrowserTtl", [value]))

    @jsii.member(jsii_name="putCacheKey")
    def put_cache_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKey, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc63d1883c581902cf872c8e4dd6836f610a288a93e2128e6611914d876a0cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCacheKey", [value]))

    @jsii.member(jsii_name="putCacheReserve")
    def put_cache_reserve(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheReserve, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1965f62742adbfb5deb80f62900d442d215e5003c81b59a00319f8fde4de9995)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCacheReserve", [value]))

    @jsii.member(jsii_name="putEdgeTtl")
    def put_edge_ttl(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtl, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7def56a1993f2605c58fb72c4db7d77b861300c3e5f873e46aa64bc5c17ee2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEdgeTtl", [value]))

    @jsii.member(jsii_name="putFromList")
    def put_from_list(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromListStruct, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a666e699f3d133ad31c8ea6908e1c22cc80be5de321583e261b7f20a4d34f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFromList", [value]))

    @jsii.member(jsii_name="putFromValue")
    def put_from_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e44fc45a1cc019c1df5eea5c5f055dbdf11d92af7da734a4d70adfc7e52c710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFromValue", [value]))

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersHeaders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a2a2268d65b8ff60992ee857ac3de2a16987bc0c7284905092fce377644b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putMatchedData")
    def put_matched_data(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersMatchedData, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603288bbd298ec391c5808de9d06fbfc6ab941ff307a7bc4b84f59bf66368253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchedData", [value]))

    @jsii.member(jsii_name="putOrigin")
    def put_origin(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOrigin, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e740b03ae9f87dca4fada4913eb258eb4b01753acd7faa0ba5dc9f8e501599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrigin", [value]))

    @jsii.member(jsii_name="putOverrides")
    def put_overrides(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverrides", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be4bd718a8ad74c3ff76fb5cd2a1e8f8d1d5bd28598240c0a44b113636a27ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverrides", [value]))

    @jsii.member(jsii_name="putResponse")
    def put_response(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersResponse", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b6140a8d3f2484a1102294eb6d7aef3531dc7aa3af13eb5810f11ab855aea4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponse", [value]))

    @jsii.member(jsii_name="putServeStale")
    def put_serve_stale(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersServeStale", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c7c3c714ed5ce09d76f9e1392a37fb89db2b5e0a5bb15d1ceb7a6590ac1c098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServeStale", [value]))

    @jsii.member(jsii_name="putSni")
    def put_sni(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersSni", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f678fc6b262e5a71a88172ccbfd657bd7624d422f6b03a72f272609b3e9a9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSni", [value]))

    @jsii.member(jsii_name="putUri")
    def put_uri(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUri", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f059292c55548b70cd94812d9cb27adb8513559a07eb3b324024bbc7db27f9bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUri", [value]))

    @jsii.member(jsii_name="resetAdditionalCacheablePorts")
    def reset_additional_cacheable_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCacheablePorts", []))

    @jsii.member(jsii_name="resetAlgorithms")
    def reset_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithms", []))

    @jsii.member(jsii_name="resetAutomaticHttpsRewrites")
    def reset_automatic_https_rewrites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticHttpsRewrites", []))

    @jsii.member(jsii_name="resetAutominify")
    def reset_autominify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutominify", []))

    @jsii.member(jsii_name="resetBic")
    def reset_bic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBic", []))

    @jsii.member(jsii_name="resetBrowserTtl")
    def reset_browser_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserTtl", []))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetCacheKey")
    def reset_cache_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKey", []))

    @jsii.member(jsii_name="resetCacheReserve")
    def reset_cache_reserve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheReserve", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCookieFields")
    def reset_cookie_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieFields", []))

    @jsii.member(jsii_name="resetDisableApps")
    def reset_disable_apps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApps", []))

    @jsii.member(jsii_name="resetDisableRailgun")
    def reset_disable_railgun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRailgun", []))

    @jsii.member(jsii_name="resetDisableRum")
    def reset_disable_rum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRum", []))

    @jsii.member(jsii_name="resetDisableZaraz")
    def reset_disable_zaraz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableZaraz", []))

    @jsii.member(jsii_name="resetEdgeTtl")
    def reset_edge_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeTtl", []))

    @jsii.member(jsii_name="resetEmailObfuscation")
    def reset_email_obfuscation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailObfuscation", []))

    @jsii.member(jsii_name="resetFonts")
    def reset_fonts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFonts", []))

    @jsii.member(jsii_name="resetFromList")
    def reset_from_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromList", []))

    @jsii.member(jsii_name="resetFromValue")
    def reset_from_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromValue", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetHotlinkProtection")
    def reset_hotlink_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHotlinkProtection", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncrement")
    def reset_increment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncrement", []))

    @jsii.member(jsii_name="resetMatchedData")
    def reset_matched_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchedData", []))

    @jsii.member(jsii_name="resetMirage")
    def reset_mirage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirage", []))

    @jsii.member(jsii_name="resetOpportunisticEncryption")
    def reset_opportunistic_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpportunisticEncryption", []))

    @jsii.member(jsii_name="resetOrigin")
    def reset_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigin", []))

    @jsii.member(jsii_name="resetOriginCacheControl")
    def reset_origin_cache_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginCacheControl", []))

    @jsii.member(jsii_name="resetOriginErrorPagePassthru")
    def reset_origin_error_page_passthru(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginErrorPagePassthru", []))

    @jsii.member(jsii_name="resetOverrides")
    def reset_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrides", []))

    @jsii.member(jsii_name="resetPhases")
    def reset_phases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhases", []))

    @jsii.member(jsii_name="resetPolish")
    def reset_polish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolish", []))

    @jsii.member(jsii_name="resetProducts")
    def reset_products(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProducts", []))

    @jsii.member(jsii_name="resetReadTimeout")
    def reset_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadTimeout", []))

    @jsii.member(jsii_name="resetRequestFields")
    def reset_request_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestFields", []))

    @jsii.member(jsii_name="resetRespectStrongEtags")
    def reset_respect_strong_etags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRespectStrongEtags", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @jsii.member(jsii_name="resetResponseFields")
    def reset_response_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseFields", []))

    @jsii.member(jsii_name="resetRocketLoader")
    def reset_rocket_loader(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRocketLoader", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetRuleset")
    def reset_ruleset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleset", []))

    @jsii.member(jsii_name="resetRulesets")
    def reset_rulesets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRulesets", []))

    @jsii.member(jsii_name="resetSecurityLevel")
    def reset_security_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityLevel", []))

    @jsii.member(jsii_name="resetServerSideExcludes")
    def reset_server_side_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideExcludes", []))

    @jsii.member(jsii_name="resetServeStale")
    def reset_serve_stale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServeStale", []))

    @jsii.member(jsii_name="resetSni")
    def reset_sni(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSni", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetSxg")
    def reset_sxg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSxg", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="algorithms")
    def algorithms(self) -> RulesetRulesActionParametersAlgorithmsList:
        return typing.cast(RulesetRulesActionParametersAlgorithmsList, jsii.get(self, "algorithms"))

    @builtins.property
    @jsii.member(jsii_name="autominify")
    def autominify(self) -> RulesetRulesActionParametersAutominifyList:
        return typing.cast(RulesetRulesActionParametersAutominifyList, jsii.get(self, "autominify"))

    @builtins.property
    @jsii.member(jsii_name="browserTtl")
    def browser_ttl(self) -> RulesetRulesActionParametersBrowserTtlList:
        return typing.cast(RulesetRulesActionParametersBrowserTtlList, jsii.get(self, "browserTtl"))

    @builtins.property
    @jsii.member(jsii_name="cacheKey")
    def cache_key(self) -> RulesetRulesActionParametersCacheKeyList:
        return typing.cast(RulesetRulesActionParametersCacheKeyList, jsii.get(self, "cacheKey"))

    @builtins.property
    @jsii.member(jsii_name="cacheReserve")
    def cache_reserve(self) -> RulesetRulesActionParametersCacheReserveList:
        return typing.cast(RulesetRulesActionParametersCacheReserveList, jsii.get(self, "cacheReserve"))

    @builtins.property
    @jsii.member(jsii_name="edgeTtl")
    def edge_ttl(self) -> RulesetRulesActionParametersEdgeTtlList:
        return typing.cast(RulesetRulesActionParametersEdgeTtlList, jsii.get(self, "edgeTtl"))

    @builtins.property
    @jsii.member(jsii_name="fromList")
    def from_list(self) -> RulesetRulesActionParametersFromListStructList:
        return typing.cast(RulesetRulesActionParametersFromListStructList, jsii.get(self, "fromList"))

    @builtins.property
    @jsii.member(jsii_name="fromValue")
    def from_value(self) -> RulesetRulesActionParametersFromValueList:
        return typing.cast(RulesetRulesActionParametersFromValueList, jsii.get(self, "fromValue"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> RulesetRulesActionParametersHeadersList:
        return typing.cast(RulesetRulesActionParametersHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="matchedData")
    def matched_data(self) -> RulesetRulesActionParametersMatchedDataList:
        return typing.cast(RulesetRulesActionParametersMatchedDataList, jsii.get(self, "matchedData"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> RulesetRulesActionParametersOriginList:
        return typing.cast(RulesetRulesActionParametersOriginList, jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="overrides")
    def overrides(self) -> "RulesetRulesActionParametersOverridesList":
        return typing.cast("RulesetRulesActionParametersOverridesList", jsii.get(self, "overrides"))

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> "RulesetRulesActionParametersResponseList":
        return typing.cast("RulesetRulesActionParametersResponseList", jsii.get(self, "response"))

    @builtins.property
    @jsii.member(jsii_name="serveStale")
    def serve_stale(self) -> "RulesetRulesActionParametersServeStaleList":
        return typing.cast("RulesetRulesActionParametersServeStaleList", jsii.get(self, "serveStale"))

    @builtins.property
    @jsii.member(jsii_name="sni")
    def sni(self) -> "RulesetRulesActionParametersSniList":
        return typing.cast("RulesetRulesActionParametersSniList", jsii.get(self, "sni"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> "RulesetRulesActionParametersUriList":
        return typing.cast("RulesetRulesActionParametersUriList", jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="additionalCacheablePortsInput")
    def additional_cacheable_ports_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "additionalCacheablePortsInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithmsInput")
    def algorithms_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]], jsii.get(self, "algorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewritesInput")
    def automatic_https_rewrites_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "automaticHttpsRewritesInput"))

    @builtins.property
    @jsii.member(jsii_name="autominifyInput")
    def autominify_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]], jsii.get(self, "autominifyInput"))

    @builtins.property
    @jsii.member(jsii_name="bicInput")
    def bic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bicInput"))

    @builtins.property
    @jsii.member(jsii_name="browserTtlInput")
    def browser_ttl_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]], jsii.get(self, "browserTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cacheInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyInput")
    def cache_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]], jsii.get(self, "cacheKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheReserveInput")
    def cache_reserve_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]], jsii.get(self, "cacheReserveInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieFieldsInput")
    def cookie_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cookieFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="disableAppsInput")
    def disable_apps_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableAppsInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRailgunInput")
    def disable_railgun_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableRailgunInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRumInput")
    def disable_rum_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableRumInput"))

    @builtins.property
    @jsii.member(jsii_name="disableZarazInput")
    def disable_zaraz_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableZarazInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeTtlInput")
    def edge_ttl_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]], jsii.get(self, "edgeTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="emailObfuscationInput")
    def email_obfuscation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "emailObfuscationInput"))

    @builtins.property
    @jsii.member(jsii_name="fontsInput")
    def fonts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fontsInput"))

    @builtins.property
    @jsii.member(jsii_name="fromListInput")
    def from_list_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]], jsii.get(self, "fromListInput"))

    @builtins.property
    @jsii.member(jsii_name="fromValueInput")
    def from_value_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]], jsii.get(self, "fromValueInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtectionInput")
    def hotlink_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hotlinkProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="incrementInput")
    def increment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "incrementInput"))

    @builtins.property
    @jsii.member(jsii_name="matchedDataInput")
    def matched_data_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]], jsii.get(self, "matchedDataInput"))

    @builtins.property
    @jsii.member(jsii_name="mirageInput")
    def mirage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mirageInput"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryptionInput")
    def opportunistic_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "opportunisticEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="originCacheControlInput")
    def origin_cache_control_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "originCacheControlInput"))

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassthruInput")
    def origin_error_page_passthru_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "originErrorPagePassthruInput"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="overridesInput")
    def overrides_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverrides"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverrides"]]], jsii.get(self, "overridesInput"))

    @builtins.property
    @jsii.member(jsii_name="phasesInput")
    def phases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "phasesInput"))

    @builtins.property
    @jsii.member(jsii_name="polishInput")
    def polish_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "polishInput"))

    @builtins.property
    @jsii.member(jsii_name="productsInput")
    def products_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productsInput"))

    @builtins.property
    @jsii.member(jsii_name="readTimeoutInput")
    def read_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="requestFieldsInput")
    def request_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtagsInput")
    def respect_strong_etags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "respectStrongEtagsInput"))

    @builtins.property
    @jsii.member(jsii_name="responseFieldsInput")
    def response_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="rocketLoaderInput")
    def rocket_loader_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rocketLoaderInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesetInput")
    def ruleset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rulesetInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesetsInput")
    def rulesets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rulesetsInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="securityLevelInput")
    def security_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideExcludesInput")
    def server_side_excludes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "serverSideExcludesInput"))

    @builtins.property
    @jsii.member(jsii_name="serveStaleInput")
    def serve_stale_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersServeStale"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersServeStale"]]], jsii.get(self, "serveStaleInput"))

    @builtins.property
    @jsii.member(jsii_name="sniInput")
    def sni_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersSni"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersSni"]]], jsii.get(self, "sniInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="sxgInput")
    def sxg_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sxgInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUri"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUri"]]], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalCacheablePorts")
    def additional_cacheable_ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "additionalCacheablePorts"))

    @additional_cacheable_ports.setter
    def additional_cacheable_ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c70c141d15e6fba80ff6d26b5b001fabb33613fc6be2fd64b660aa5ae6d25b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalCacheablePorts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewrites")
    def automatic_https_rewrites(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "automaticHttpsRewrites"))

    @automatic_https_rewrites.setter
    def automatic_https_rewrites(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b211a463ee99fcd38484a48f3c399af92c95e2fdacd72e31ec1c2077f40336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticHttpsRewrites", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bic")
    def bic(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "bic"))

    @bic.setter
    def bic(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5fa057d561e1e0e156c5d6ba189df1696b28d0050888930aa10ae456f477f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bic", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cache"))

    @cache.setter
    def cache(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67ee1f2c3423c8c27aff273783924f9a5166519128d5c5deb7e6ba9bc7479f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cache", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25acdb5536551121106a45692e244114bdae17ac486743727919ce60d39b4900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b036f29847efe4a4d4dd3bd0fa7806cc6b72e5f0ef3daaca282b882371d845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cookieFields")
    def cookie_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cookieFields"))

    @cookie_fields.setter
    def cookie_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14e72f6a3a3ede57b891a1a294a8aa05790786a930a0256f0de02a87a070b260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieFields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableApps")
    def disable_apps(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableApps"))

    @disable_apps.setter
    def disable_apps(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b045f588396b62337e9e49757f4e4c1d0269dee5b84092a75857a34426f6ac07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApps", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableRailgun")
    def disable_railgun(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableRailgun"))

    @disable_railgun.setter
    def disable_railgun(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d8ca79dfd28d97b02d00e46d25bc47d1b606ab2154bc40ec47ae9c618f76187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRailgun", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableRum")
    def disable_rum(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableRum"))

    @disable_rum.setter
    def disable_rum(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69a25df6053b939d833ef898cd9d3b6d593c9840137beb9df02aa8f17e270249)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRum", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableZaraz")
    def disable_zaraz(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableZaraz"))

    @disable_zaraz.setter
    def disable_zaraz(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0503c6462ca0cc885dbbf47627a5a892f70060ae9e22761f114ec9ed562cb1f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableZaraz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="emailObfuscation")
    def email_obfuscation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "emailObfuscation"))

    @email_obfuscation.setter
    def email_obfuscation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de03fd0bea7959103ee49f66cffff9443af5f7b3decd178e38e7fefdf31dfd59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailObfuscation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fonts")
    def fonts(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fonts"))

    @fonts.setter
    def fonts(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b7bc956f570b3f71a8c0f6e021433f2bd67d97a20fb1f05b3e82e07b0b696d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fonts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @host_header.setter
    def host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__595e4e501b488cd0a2a89462aaf3a1c0dafe61f0d852a707b0e7af252c518e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeader", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtection")
    def hotlink_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hotlinkProtection"))

    @hotlink_protection.setter
    def hotlink_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd27419be9bd0141c30e599024e5f3a9bae37e3e0c5417630274afa6c7264f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hotlinkProtection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c36a64d1a2cda8b8450f543be75de2ecbb4ec96e8b5a48bb7e975a19d1189c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="increment")
    def increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "increment"))

    @increment.setter
    def increment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8725fab92f8c931508a4c990fb0030902d4b7f7c60321a25e6cf8ee81d57defd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "increment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mirage")
    def mirage(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mirage"))

    @mirage.setter
    def mirage(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef36b756b3e0b775cd19c59d56a5440998bbd7721f7617245ba2b02259c510a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirage", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryption")
    def opportunistic_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "opportunisticEncryption"))

    @opportunistic_encryption.setter
    def opportunistic_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad32a10d8350bf6127cbef96327b8784bffb7b967a347b3ba121a89e30d309d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opportunisticEncryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originCacheControl")
    def origin_cache_control(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "originCacheControl"))

    @origin_cache_control.setter
    def origin_cache_control(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212a8ecbec2867d18f7b02f1a46f0ef109870d85b245f1a361e78189600ae53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originCacheControl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassthru")
    def origin_error_page_passthru(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "originErrorPagePassthru"))

    @origin_error_page_passthru.setter
    def origin_error_page_passthru(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8789c7f1457fcfaf3f4002826d68697627ab6ece207fe56f60822436f36eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originErrorPagePassthru", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phases")
    def phases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "phases"))

    @phases.setter
    def phases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142a215c62758d408656d18d174b7f0412278d46902198af8ddc2d6a6fbbdb29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phases", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="polish")
    def polish(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "polish"))

    @polish.setter
    def polish(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3267a60274b1664f20a4b469facd3e81b98007c4557fe846a529c2e61eb9bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "polish", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="products")
    def products(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "products"))

    @products.setter
    def products(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d1a161bdac9b62e2298ea5c9ee5b80797e01c6f30fb3034b7ab72847d4ccbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "products", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readTimeout")
    def read_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readTimeout"))

    @read_timeout.setter
    def read_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e6a64fd066c8a5bfc912e2dd835a395e9a49a39fa9b73e54409cc062efc6918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readTimeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestFields")
    def request_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestFields"))

    @request_fields.setter
    def request_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5ed38becf243013f7d4d12b323d06d1466f18c998f5b55ce963be740dcf893)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestFields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtags")
    def respect_strong_etags(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "respectStrongEtags"))

    @respect_strong_etags.setter
    def respect_strong_etags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa25cb0d5eada83326490127860c9e87b5da028ee760d21605d133a1cf92f26c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "respectStrongEtags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="responseFields")
    def response_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseFields"))

    @response_fields.setter
    def response_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40de264f8a38f541533927727562082f6ab023b0a555883efb014d146e84fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseFields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rocketLoader")
    def rocket_loader(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rocketLoader"))

    @rocket_loader.setter
    def rocket_loader(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c3ca2d0ac3819e9ab928bf9fa162f6d5c8f190352e9937fd1eec12a3e07e7d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rocketLoader", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ccba8efdcccec9bef2204ee4a12cdfd4e7b8da209c81c4346a27cf1224eb871)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleset")
    def ruleset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleset"))

    @ruleset.setter
    def ruleset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9387c1cb07b59d08ec8e60a890d22a4240518137d2ec84f52411c4e8d19f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleset", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rulesets")
    def rulesets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rulesets"))

    @rulesets.setter
    def rulesets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1744824af7da4382968436ab7387d37c00778fad30941f7f5adf39bbe54eef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rulesets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23571c327a3a608db8886935622d5deb109d7acc36016503e3c3ab32c93cd2ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSideExcludes")
    def server_side_excludes(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "serverSideExcludes"))

    @server_side_excludes.setter
    def server_side_excludes(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f9dcfb6206b557a2796b90e02bcf869bc1138f101eceefdf962940441ad13db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideExcludes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da6500381dedb9c95a466d072c2e57cd23d0444d02d98ab8ac63740e7962b7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be717b9be7fc1946d5d943892d1f46ea02c6140c3ae620d0fba2ab46aff00a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sxg")
    def sxg(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sxg"))

    @sxg.setter
    def sxg(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23836a04174f99cee04cc396ab3fa32231f2f7b0f4f463782757304a50cb0b25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sxg", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParameters]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParameters]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParameters]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a644324f3a0583755f6708bb7c316e8a126bd4a604f0950e0303d26cf3b3789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverrides",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "categories": "categories",
        "enabled": "enabled",
        "rules": "rules",
        "sensitivity_level": "sensitivityLevel",
    },
)
class RulesetRulesActionParametersOverrides:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        categories: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesCategories", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sensitivity_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the rule-level override. Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        :param categories: categories block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#categories Ruleset#categories}
        :param enabled: Defines if the current ruleset-level override enables or disables the ruleset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        :param rules: rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        :param sensitivity_level: Sensitivity level to override for all ruleset rules. Available values: ``default``, ``medium``, ``low``, ``eoff``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sensitivity_level Ruleset#sensitivity_level}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289b231a63801bfc94b417b219a571458a2f775e9df8435517ca5141004b90aa)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument categories", value=categories, expected_type=type_hints["categories"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument sensitivity_level", value=sensitivity_level, expected_type=type_hints["sensitivity_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if categories is not None:
            self._values["categories"] = categories
        if enabled is not None:
            self._values["enabled"] = enabled
        if rules is not None:
            self._values["rules"] = rules
        if sensitivity_level is not None:
            self._values["sensitivity_level"] = sensitivity_level

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the rule-level override.

        Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def categories(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesCategories"]]]:
        '''categories block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#categories Ruleset#categories}
        '''
        result = self._values.get("categories")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesCategories"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines if the current ruleset-level override enables or disables the ruleset.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]], result)

    @builtins.property
    def sensitivity_level(self) -> typing.Optional[builtins.str]:
        '''Sensitivity level to override for all ruleset rules. Available values: ``default``, ``medium``, ``low``, ``eoff``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sensitivity_level Ruleset#sensitivity_level}
        '''
        result = self._values.get("sensitivity_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategories",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "category": "category", "enabled": "enabled"},
)
class RulesetRulesActionParametersOverridesCategories:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        category: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param action: Action to perform in the tag-level override. Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        :param category: Tag name to apply the ruleset rule override to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#category Ruleset#category}
        :param enabled: Defines if the current tag-level override enables or disables the ruleset rules with the specified tag. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870a3e9613b3055d66a04e84190aa900e35ca00b4179c5f914b92b850ff0d78d)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if category is not None:
            self._values["category"] = category
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the tag-level override.

        Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        '''Tag name to apply the ruleset rule override to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#category Ruleset#category}
        '''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines if the current tag-level override enables or disables the ruleset rules with the specified tag.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverridesCategories(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOverridesCategoriesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategoriesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb5d6d7c449a715de0d634766afeaf11ea29bd26183066a79f47e48a29283c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOverridesCategoriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26dd08b921db6db4613fab63c27b1239a65774fa637f1e2faddc664c5826fbe7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOverridesCategoriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c825eb95aab5218b959203ff797d71420b620da86966c7f60d29dbcb6bacc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913fbcb3ed99a8c4e13200e8400020909d32532901ba819ab6eba631ec73e26e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07fa4407817774bdfaa7f1febc82d4ae1bd04203c05546046a8397def461ca00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada2b6725872dbbea5aefde73064d3d4cd92ba613eaa5a54071545b2297fee54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOverridesCategoriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategoriesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402f123ba7682883847c231fb72fd3f1ebefd584ed8452dd982abcb6cddad180)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetCategory")
    def reset_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategory", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06dd0e40b1bbbeb6ed1b838f84f8f022bcd0f6e25aa52d0f802317bceef9338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286a0fb32ec1b6fb46ec53b9aa8821dafb847cc73662be6df854bbb9fa3d6511)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd740b3b216fccf1734a09f57bc3f8893e2a873f04312213b3ffb8767a2e3885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesCategories]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesCategories]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesCategories]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd79b3b5f8aafd85e5a10caf3324fbe20cbd9cfa32db38492719881c59eff882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOverridesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad927ed30b4f4f6568a2db00510ef7da84e3c5ae5d00f6e2a33ecc1f7aedddc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOverridesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e686bcdb5011c4eecba9d2c5153499ad18cb868617580b81ec872d61d830c174)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOverridesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c91a5254034c6ec40dff67cb48b6c88bb221930a4c2ad5addb2c69ae61c0f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3b6d42b83ff9d2852798fc3f44f0384978e15d970b25905a990c3ff80bf8fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bc1cca55c1cf767737e562e0a2345e44197f70ec6c939b61f7b1e101fcd94c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverrides]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverrides]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverrides]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f330bbac42a4a96e19690215dd6ba16bf42e6ef4c448760822807bdb91816419)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOverridesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4a75bfebf22520c432fb864d164587dfc6629af51c741571d1cae0dc473891)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCategories")
    def put_categories(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesCategories, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f91dbcb328e5fe67c74764d783254676c987ddc83f84e5d0f4250c0f2e7164)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCategories", [value]))

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49231c10b47845919778a3ff0cd8cb45e4ff12408921d44c284253f402792c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetCategories")
    def reset_categories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategories", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetSensitivityLevel")
    def reset_sensitivity_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitivityLevel", []))

    @builtins.property
    @jsii.member(jsii_name="categories")
    def categories(self) -> RulesetRulesActionParametersOverridesCategoriesList:
        return typing.cast(RulesetRulesActionParametersOverridesCategoriesList, jsii.get(self, "categories"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "RulesetRulesActionParametersOverridesRulesList":
        return typing.cast("RulesetRulesActionParametersOverridesRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="categoriesInput")
    def categories_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]], jsii.get(self, "categoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevelInput")
    def sensitivity_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sensitivityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c3571bd1397f3f382e68340ab32ef7a523fced2352e8530cf59a4ddc325b4b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb3c647c13014dfca348295da7d04550c088169dc31c683d9021fc61602644e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevel")
    def sensitivity_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sensitivityLevel"))

    @sensitivity_level.setter
    def sensitivity_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ef3a813e5713623177c0367d964f6f28b2be05033a87466fa361a71fc3da89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitivityLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverrides]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverrides]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverrides]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c9c29a54937eeffd9bbffd7ee83cd758e4eb9821f76e4503355534c4010b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRules",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "enabled": "enabled",
        "id": "id",
        "score_threshold": "scoreThreshold",
        "sensitivity_level": "sensitivityLevel",
    },
)
class RulesetRulesActionParametersOverridesRules:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        score_threshold: typing.Optional[jsii.Number] = None,
        sensitivity_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the rule-level override. Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        :param enabled: Defines if the current rule-level override enables or disables the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        :param id: Rule ID to apply the override to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#id Ruleset#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param score_threshold: Anomaly score threshold to apply in the ruleset rule override. Only applicable to modsecurity-based rulesets. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_threshold Ruleset#score_threshold}
        :param sensitivity_level: Sensitivity level for a ruleset rule override. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sensitivity_level Ruleset#sensitivity_level}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d719fd0336c6ca82eeb45415fc6fb6c6e6baa00e20ad4c5194223a1ddb5772e6)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument score_threshold", value=score_threshold, expected_type=type_hints["score_threshold"])
            check_type(argname="argument sensitivity_level", value=sensitivity_level, expected_type=type_hints["sensitivity_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if score_threshold is not None:
            self._values["score_threshold"] = score_threshold
        if sensitivity_level is not None:
            self._values["sensitivity_level"] = sensitivity_level

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the rule-level override.

        Available values: ``block``, ``challenge``, ``compress_response``, ``ddos_dynamic``, ``ddos_mitigation``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``serve_error``, ``set_cache_settings``, ``set_config``, ``skip``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines if the current rule-level override enables or disables the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Rule ID to apply the override to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#id Ruleset#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def score_threshold(self) -> typing.Optional[jsii.Number]:
        '''Anomaly score threshold to apply in the ruleset rule override. Only applicable to modsecurity-based rulesets.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_threshold Ruleset#score_threshold}
        '''
        result = self._values.get("score_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sensitivity_level(self) -> typing.Optional[builtins.str]:
        '''Sensitivity level for a ruleset rule override.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#sensitivity_level Ruleset#sensitivity_level}
        '''
        result = self._values.get("sensitivity_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverridesRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOverridesRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRulesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01983b963396a95702e44122c05081ecf289f27203551a2d4aca8e0be5c1b36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOverridesRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f152a794bed77dc33c6a8d522be32f6240105918ff99cbf3539a3b8958d7e9e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOverridesRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0376d1f99cce300788c8a55376487982090f60faf371b146407d3adc33e98f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b46926039e7e4361be6e6ddf5b42573fba9694d6e77e75ac6dd6876041db61b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd6f32d3e802d8787776f8358501880e6226c4774d9236922e1b8b0e4d83cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a015621ebad45cd200a387d33eaf9893c89c3d5eb8a5c208c37022fe5990ebe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersOverridesRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRulesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a94fced77c1118bfb0394614428707b6a1e5bc17a6a17a634d3b22cc647d7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScoreThreshold")
    def reset_score_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoreThreshold", []))

    @jsii.member(jsii_name="resetSensitivityLevel")
    def reset_sensitivity_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitivityLevel", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="scoreThresholdInput")
    def score_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scoreThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevelInput")
    def sensitivity_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sensitivityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd03cd7b8ae2161dcc516a76373f45d43c12d45a4fe4d12d854ece8771164810)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecfc2aa84edb5d0d5b7c7c50ed56b5daee3e9acadabc79ff642b4f84cb967ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f4e4b28eeeea751243819793b76580b5ea3c634903f942afacdd666f12bd3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scoreThreshold")
    def score_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scoreThreshold"))

    @score_threshold.setter
    def score_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4e6b9ada3086f9c3babd33bc6f4f5d7ac4a0ac56e75114687c38140d8ebba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoreThreshold", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevel")
    def sensitivity_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sensitivityLevel"))

    @sensitivity_level.setter
    def sensitivity_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b2e50085ddd09296f10dbc42f17467188e97e556d33d3dc45f2081dcb22573d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitivityLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d61b1f50416d66569c28bd50db859969c72a731dbc51e960869bf8a7ef51688)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponse",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "status_code": "statusCode",
    },
)
class RulesetRulesActionParametersResponse:
    def __init__(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Body content to include in the response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content Ruleset#content}
        :param content_type: HTTP content type to send in the response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content_type Ruleset#content_type}
        :param status_code: HTTP status code to send in the response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8500309c03e45915aabd35e7391cff360150a44d7935ae6d114d7e712875932)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content is not None:
            self._values["content"] = content
        if content_type is not None:
            self._values["content_type"] = content_type
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Body content to include in the response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content Ruleset#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''HTTP content type to send in the response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#content_type Ruleset#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''HTTP status code to send in the response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersResponseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponseList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ff9889f313565d9195aafbb295c205e8c17b1f1bb84c4226d033e2961776f4e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersResponseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5959c7e9b061c8e66122a056752a0aceca71046c9bc887ce65bbebe9bfeba54d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersResponseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7294e3563e074fad1699be7810162951a75e3fe366b0803812685cebbcbf071b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bbae99f322aba3a6071f68bd369dfa277e1d2ddd8bcc549269df1b650c1e742)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d954a427499852fe0c5c65ec93c4ce7b27fa7c7ea506c3233948bd3159762f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersResponse]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersResponse]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersResponse]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c6479bf7dc277023c2ec5cb54106423f052c751cde054a056badfea8a9ee4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersResponseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponseOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d828939b8540c63d20da5a88a1d11fe8a6b8ed5126a9828bb92e9e64387e5758)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdf12fabbfc8ec3caa72fc5163fa719866864783fce5c7e83513165b9e8fed82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80dc442ad7b77f1f03f573a2afc17acd6a921bd2e28bac18b10bd3cdafd72600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b469c3a82ebd109abcbf69cd9a73d38bcfd4129e4c0dfa670b29cb5e4fcef24e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersResponse]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersResponse]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersResponse]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a03892bf374fe4ba6438d6b5241fd066e843add6b3029ccaf63d66e3d41761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersServeStale",
    jsii_struct_bases=[],
    name_mapping={"disable_stale_while_updating": "disableStaleWhileUpdating"},
)
class RulesetRulesActionParametersServeStale:
    def __init__(
        self,
        *,
        disable_stale_while_updating: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param disable_stale_while_updating: Disable stale while updating. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_stale_while_updating Ruleset#disable_stale_while_updating}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6af794003f1fe3b30a4b979ab5d9747ad2e604f15a44e341b1f9fc74ff80687)
            check_type(argname="argument disable_stale_while_updating", value=disable_stale_while_updating, expected_type=type_hints["disable_stale_while_updating"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disable_stale_while_updating is not None:
            self._values["disable_stale_while_updating"] = disable_stale_while_updating

    @builtins.property
    def disable_stale_while_updating(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Disable stale while updating.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#disable_stale_while_updating Ruleset#disable_stale_while_updating}
        '''
        result = self._values.get("disable_stale_while_updating")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersServeStale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersServeStaleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersServeStaleList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcda3679642af7e720ab9e7016ddbdec9a825a30383124f531eb53444cacde89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersServeStaleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1762de37fe78b51512d10d47017c77824472412303df61120de92f01dd895e97)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersServeStaleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__418dbcc20e9b1d0a8711363262d1c782b28f475064baf64d02dfb65956e40b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeabc0973390ed2fc1e8b9e3318aa2eb315bcff02dc348c29c24deb94a115b59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7817663479b09bde25a77fd90ec8ab72375a5ae3538360df2be9fb0389fbf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersServeStale]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersServeStale]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersServeStale]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1f438c4b1134536ea853558e11f7004abed04014c7027cfac3d7dbe3c5a92f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersServeStaleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersServeStaleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8e58da406be38d9a7a0f737278761b2c34664b670b7f429dfbd3b22119c596)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableStaleWhileUpdating")
    def reset_disable_stale_while_updating(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableStaleWhileUpdating", []))

    @builtins.property
    @jsii.member(jsii_name="disableStaleWhileUpdatingInput")
    def disable_stale_while_updating_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableStaleWhileUpdatingInput"))

    @builtins.property
    @jsii.member(jsii_name="disableStaleWhileUpdating")
    def disable_stale_while_updating(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableStaleWhileUpdating"))

    @disable_stale_while_updating.setter
    def disable_stale_while_updating(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9edf835625c088bf50a4f8bc8f239e9b5a8a81302584f4efe0fab9547d1f9180)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableStaleWhileUpdating", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersServeStale]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersServeStale]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersServeStale]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86250fe3ceb4eeb3c4ed04c9bc38212c7c77f6f5d6fa904b714e2719a3384263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersSni",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class RulesetRulesActionParametersSni:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Value to define for SNI. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec0b9d1ca4750f04b5189f1e472b6d5829ff6c7b4d7d1320ecb693673f8995e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value to define for SNI.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersSni(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersSniList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersSniList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b1f07fd35aa64a6f5a804c503bdcd071e0253b370cf504c416b7365fb96ffd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersSniOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2d244ece81677141f520c8c4f3b4538fec63b2fce5994f7adf2c06d3fa37a8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersSniOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf0defe3b44330cfdcac9965d070f7efe4b4ef7a9f570d78bc22c352b7686a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704e0ed0bbae97988539648897dca4ddd2f77f83782ca985c7d63d39778eb274)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f80659f8de0bb2997720b146321dad67156b5f4bab77ea98086ff1c45b1a6b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersSni]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersSni]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersSni]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d81ea933adf0ff4f7dd4f637710517268cd295d8e5d6288fdf5f5397c64152c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersSniOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersSniOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b927797a5318e3fe56d152556b11869b432f4eff52ecb15a4725d4845cbafd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__decf557748c3f6266ab6417fc1ec5b87e698c3ecdc4e4837dbe7062d644f2d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersSni]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersSni]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersSni]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026a8ff5b9c8de71b3bfd70fbe23ee887cd28add0f0052d324449e2b1ccf6212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUri",
    jsii_struct_bases=[],
    name_mapping={"origin": "origin", "path": "path", "query": "query"},
)
class RulesetRulesActionParametersUri:
    def __init__(
        self,
        *,
        origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        path: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUriPath", typing.Dict[builtins.str, typing.Any]]]]] = None,
        query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUriQuery", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param origin: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin Ruleset#origin}.
        :param path: path block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#path Ruleset#path}
        :param query: query block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#query Ruleset#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7637f849e9379913b2b8491c44cffba72ac1044fed31376469b3ffb819976c70)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if origin is not None:
            self._values["origin"] = origin
        if path is not None:
            self._values["path"] = path
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def origin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#origin Ruleset#origin}.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def path(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriPath"]]]:
        '''path block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#path Ruleset#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriPath"]]], result)

    @builtins.property
    def query(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriQuery"]]]:
        '''query block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#query Ruleset#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriQuery"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247df54c4f268d519dda0282d940a8e29346fb25b668c9c76d31499c0730d5b1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersUriOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df20e935ca559c1a9973dd3be551b2cfbf1cfd05a3d007364c6fae84164278fb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersUriOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa81845a820cf29589dea9dffc7a701d6e2f0136e81042e20a45464ebcd05fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4837fb9397023f8f441892a5b877eb2ee7e2bff8604106186ee8a8cf00afdc80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94ebb647f93ab3a3f04f29a878b9abaa16a06d0308ed22597552ad83063d376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUri]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUri]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUri]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac76a5ed7bc45921cc2c1991c3eff6d4cbc55a5c9934f1d9c31babdcac25176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersUriOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e144d3dff4777b08e8aeeb362733a5f87dbbbf25f2bd9b516614e2c80bc54f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUriPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a993610f47c8c4dff9c33c9aa9efa51ffdfbdecdb141484953edbe054da709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersUriQuery", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f1ef2eff78798976148f9e1efaea462f2a904b3e27b92096bba5eb8cf58d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQuery", [value]))

    @jsii.member(jsii_name="resetOrigin")
    def reset_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigin", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "RulesetRulesActionParametersUriPathList":
        return typing.cast("RulesetRulesActionParametersUriPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "RulesetRulesActionParametersUriQueryList":
        return typing.cast("RulesetRulesActionParametersUriQueryList", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriPath"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesActionParametersUriQuery"]]], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "origin"))

    @origin.setter
    def origin(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ce0ce97f42c3949b13b7ae2c2c0cfb4123275b2e6862839847cad8711c399ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUri]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUri]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUri]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a4c62bcede669d486eeb42aa33382800217057612a9bfe2fea64fb179af46a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriPath",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersUriPath:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a955ee75379fbf48e07d2cbf88001509fa3f47ecc57ae58f10d7539f8362b51)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Expression that defines the updated (dynamic) value of the URI path or query string component.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static string value of the updated URI path or query string component.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriPathList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriPathList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68501674ddea9d2727ac31e37db602229142920a7bfd0fd941afd80de65f6849)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersUriPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691d6e8891f0f6af24e1953faaa457e1c76f39d0d1c7a412f12c3b528861cd72)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersUriPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5544f495fdea8c2b5e1387627444bf107ccc0a19460637d023a9ad54887e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3bdf0983039d81f4a528cbff2e8dd3fc33fcf165520cafe191ad5c06c7bf0a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713e000cf3d406c05f7f2301475d66cc3df132e9465f98971a877ed4fd787777)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriPath]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0372b739170083336fde5568727c518fadf195dfc9080ef98eb160bfef458d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersUriPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf010b3a290c16ed74ca1083e4ad536f26c20cb04de60e72ca3b5e2858f7b0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c2710cd7a4a1eb7c9f2da003bd2eab87603f7205d6657a646eab787d8ebf8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1a75c0b9c6445be820eb239229f642f66359b9ed29dab2dd00ec4ceb9f1408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriPath]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriPath]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriPath]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e72fc8a56ec40a9c549e370e9ae5b83e28859c40d324b78c59d5c1578d2a41e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriQuery",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersUriQuery:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21c1bf0e13c1ceda03583f316fe8468d17212b7e26e30d5bcf63e16d1757760)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Expression that defines the updated (dynamic) value of the URI path or query string component.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static string value of the updated URI path or query string component.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUriQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriQueryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriQueryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938629a606923dcbfb0c3fb513b70ad39434b129b0b293bec796ae595d6e6ce8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersUriQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec088b7ecb201465737352b023208328128312748b4b2d5c5f973d9deb57e2aa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersUriQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69277f448d117284b28c75eb07c22a492c523a8e74b0ad6c83a4bea2b297be3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c8496ed6d092578af403bbb3ddd11cc7bd95ee4ea4893c3835305813748a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71722b134c7a25b0a5d7f602bec329bb7dac5c8c515e9c89cf1ee4b1fbed7d43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriQuery]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a63dc2a82004727eafc326382a430a17dd931896faec6c7842de1b35f314874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesActionParametersUriQueryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriQueryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ede297a8894591be9b9c30bc9f64ebfa264571b2941de78d3c754ba1e5f286)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262195d83903840d6a099c3c7f1821aa294b2460780dd1c4432edb224532068b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16810d5ae7661aeb4c3464ef88e31bd0e8bdde48123ba75fc31aed5bc9c0eaa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriQuery]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriQuery]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriQuery]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7cfe6d676d9f0066a989d6c11b9a5ee9b0121092a73702c052d366cd21da940)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesExposedCredentialCheck",
    jsii_struct_bases=[],
    name_mapping={
        "password_expression": "passwordExpression",
        "username_expression": "usernameExpression",
    },
)
class RulesetRulesExposedCredentialCheck:
    def __init__(
        self,
        *,
        password_expression: typing.Optional[builtins.str] = None,
        username_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "password" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#password_expression Ruleset#password_expression}
        :param username_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "username" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#username_expression Ruleset#username_expression}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__956002fea91217de0bd013500bd1ef43ec0fa1bc2078234a10de02df91cc0462)
            check_type(argname="argument password_expression", value=password_expression, expected_type=type_hints["password_expression"])
            check_type(argname="argument username_expression", value=username_expression, expected_type=type_hints["username_expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if password_expression is not None:
            self._values["password_expression"] = password_expression
        if username_expression is not None:
            self._values["username_expression"] = username_expression

    @builtins.property
    def password_expression(self) -> typing.Optional[builtins.str]:
        '''Firewall Rules expression language based on Wireshark display filters for where to check for the "password" value.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#password_expression Ruleset#password_expression}
        '''
        result = self._values.get("password_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_expression(self) -> typing.Optional[builtins.str]:
        '''Firewall Rules expression language based on Wireshark display filters for where to check for the "username" value.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#username_expression Ruleset#username_expression}
        '''
        result = self._values.get("username_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesExposedCredentialCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesExposedCredentialCheckList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesExposedCredentialCheckList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5595526cc147f2f4b3f23d8e6796b5a33d33718550e7f51daebaab0c9aa59f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesExposedCredentialCheckOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c070771cd0bc5fa8a392fe76e34ce6eefd1ce34f76d50d94165b714eaaf5923)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesExposedCredentialCheckOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37c88dec41bc1ec0661928ff6f01cf35d8b897c5dea74d3fb5d2e234443818b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80454991f875c602ba0337b7b54ee644027b1402d348113c2f48d5635b1501df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63e7718c0b277563d697bbe63bc64b2d01e8ada50cadbf6ff1c44fb3a0cc3dfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2474850e5ed795ca4fe3cec0f56f9874f0baa9bdd41d57d464c1042d94313aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesExposedCredentialCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesExposedCredentialCheckOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a9b0dc4f1ff94118d2e581e0fb2256d3d6eb7e68b74e709d36deb99cc45e6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPasswordExpression")
    def reset_password_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExpression", []))

    @jsii.member(jsii_name="resetUsernameExpression")
    def reset_username_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameExpression", []))

    @builtins.property
    @jsii.member(jsii_name="passwordExpressionInput")
    def password_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameExpressionInput")
    def username_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpression")
    def password_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordExpression"))

    @password_expression.setter
    def password_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bfb41d321fcf5927e6ea78927aaa8b545d2c8760fc5b1753d92c4c27a9ad4bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExpression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="usernameExpression")
    def username_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameExpression"))

    @username_expression.setter
    def username_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6232ccb306b8b31dc67c2956febb52c394365472080160fd2d378d8de21437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameExpression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesExposedCredentialCheck]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesExposedCredentialCheck]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesExposedCredentialCheck]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4a3f117a889d41b6406bd4c8973c3668a67d92be1caa188f5a1a602cb059998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b638a57ff40e9d87e75f857c9dcf5112e9cad13a2e6f6a836f152c60ecaf62d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RulesetRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa82498c7685c5e3a26657e17a0b5281530cf63bdf27d82ff84bf9dee51562a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ec520600d8cdb68e796d3434bc7e7d88f1e6c28cd889c617a411994bc89a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7cc599c63fe0e23ac63fd5aefb176ca53d7831d0210d0ed60fd38147effee3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5529a232890ade1bb6e492549ed37ac4a9a63858de3cba7fa62164bdd8f52686)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94e3fa75e0dc8a2c0a95a56412fdfc5cea96ec8cc784cbbcc636696e9922585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesLogging",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class RulesetRulesLogging:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Override the default logging behavior when a rule is matched. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a615d8f0db2555d02e911e4d5bdb12a8a1e08d20f1dcdae89d5774dfb9adee4b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Override the default logging behavior when a rule is matched.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesLoggingList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesLoggingList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c102042ab2f01dd08439bd1049c1a8303a836d47c4adf865e2dc514d2e6a38d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RulesetRulesLoggingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d6380cf52e0d0f34fa36e9daba079adc0c79e496f02d711cfa7f4509db44d0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesLoggingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213cbf5bbf47fc09f35add293e18bf22bccf5df4648f0ae94c02630c0f55e2de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d62a9a7a01822d52b278ee0cb251f54a95eb82bb09dd95d41f934bb3e4a00bb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__410f068d5872b8a21487ccc249a4fe1d8897882b011ff9e587c84ba26182d8a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d5c8e7196e084f694ca8f11285a626ffb924e49eb5badd67b57b09d4387349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesLoggingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesLoggingOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a6be262230df1f4045ee59501803ffc3c3757d7c51b2db189d29fd1c4ecb69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31729ddd5eb3571f88bd3c3822868e036521763a96005d2b72d85de49c93b62d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesLogging]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesLogging]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesLogging]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338080b0388c6eb6ae350ac113f4dd63ecd19345043e1f0dbab773c641a7d43f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__232bfcbec9876f2e54ae7067e9d0e1b09aefe8dcf9eb73e7090575aa463eb9a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putActionParameters")
    def put_action_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParameters, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f5531cb4544db9cbbdfbfbbc0976e14d0fd92bf735ffdea7b65a5cf554651c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActionParameters", [value]))

    @jsii.member(jsii_name="putExposedCredentialCheck")
    def put_exposed_credential_check(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesExposedCredentialCheck, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd272e0a472c2853cc489063505d21a4a2c7c92a91fe883d5d1abff1c9cc743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExposedCredentialCheck", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesLogging, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a1fa5fe2dd18e82255398b45180aa2ff6a4b821e771fab5a3167b7719c06ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putRatelimit")
    def put_ratelimit(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RulesetRulesRatelimit", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e335db7da764f664bbf07dc612e19ac7eb5b56b44b8e06983c2188f9b71f6f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRatelimit", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetActionParameters")
    def reset_action_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionParameters", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExposedCredentialCheck")
    def reset_exposed_credential_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposedCredentialCheck", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetRatelimit")
    def reset_ratelimit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRatelimit", []))

    @jsii.member(jsii_name="resetRef")
    def reset_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRef", []))

    @builtins.property
    @jsii.member(jsii_name="actionParameters")
    def action_parameters(self) -> RulesetRulesActionParametersList:
        return typing.cast(RulesetRulesActionParametersList, jsii.get(self, "actionParameters"))

    @builtins.property
    @jsii.member(jsii_name="exposedCredentialCheck")
    def exposed_credential_check(self) -> RulesetRulesExposedCredentialCheckList:
        return typing.cast(RulesetRulesExposedCredentialCheckList, jsii.get(self, "exposedCredentialCheck"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> RulesetRulesLoggingList:
        return typing.cast(RulesetRulesLoggingList, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="ratelimit")
    def ratelimit(self) -> "RulesetRulesRatelimitList":
        return typing.cast("RulesetRulesRatelimitList", jsii.get(self, "ratelimit"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="actionParametersInput")
    def action_parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]], jsii.get(self, "actionParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedCredentialCheckInput")
    def exposed_credential_check_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]], jsii.get(self, "exposedCredentialCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="ratelimitInput")
    def ratelimit_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesRatelimit"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RulesetRulesRatelimit"]]], jsii.get(self, "ratelimitInput"))

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a8b2051ba3e07c8fd8efd2be9075b43c5332eb9ea5d51df10a4d77b49d545a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391a57355cb044a3d1a304c34d98e3df61c0f2d220fa879755af9013eca7f917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de4ddc321d90d7d6c8244ca6bb0ce532d0b5bba27d82bec38580fc874d181c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b149f46dbbabe23673615237b47b107721f12fd1ac7d54e6b4f3a4eb15dda3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496453f1fad09ad9a80bb1979431bc1fec98331b67f7871acffbca853e08bcc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8973b6913b6b80c7a2af15ecf906d5cbada26f8cee96a00a537f8267db359fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesRatelimit",
    jsii_struct_bases=[],
    name_mapping={
        "characteristics": "characteristics",
        "counting_expression": "countingExpression",
        "mitigation_timeout": "mitigationTimeout",
        "period": "period",
        "requests_per_period": "requestsPerPeriod",
        "requests_to_origin": "requestsToOrigin",
        "score_per_period": "scorePerPeriod",
        "score_response_header_name": "scoreResponseHeaderName",
    },
)
class RulesetRulesRatelimit:
    def __init__(
        self,
        *,
        characteristics: typing.Optional[typing.Sequence[builtins.str]] = None,
        counting_expression: typing.Optional[builtins.str] = None,
        mitigation_timeout: typing.Optional[jsii.Number] = None,
        period: typing.Optional[jsii.Number] = None,
        requests_per_period: typing.Optional[jsii.Number] = None,
        requests_to_origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        score_per_period: typing.Optional[jsii.Number] = None,
        score_response_header_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param characteristics: List of parameters that define how Cloudflare tracks the request rate for this rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#characteristics Ruleset#characteristics}
        :param counting_expression: Criteria for counting HTTP requests to trigger the Rate Limiting action. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#counting_expression Ruleset#counting_expression}
        :param mitigation_timeout: Once the request rate is reached, the Rate Limiting rule blocks further requests for the period of time defined in this field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mitigation_timeout Ruleset#mitigation_timeout}
        :param period: The period of time to consider (in seconds) when evaluating the request rate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#period Ruleset#period}
        :param requests_per_period: The number of requests over the period of time that will trigger the Rate Limiting rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#requests_per_period Ruleset#requests_per_period}
        :param requests_to_origin: Whether to include requests to origin within the Rate Limiting count. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#requests_to_origin Ruleset#requests_to_origin}
        :param score_per_period: The maximum aggregate score over the period of time that will trigger Rate Limiting rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_per_period Ruleset#score_per_period}
        :param score_response_header_name: Name of HTTP header in the response, set by the origin server, with the score for the current request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_response_header_name Ruleset#score_response_header_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9146fcba83927550bd6dd9fbb5fbeaf988f9ce03cbdc34fcc4c0127b518756)
            check_type(argname="argument characteristics", value=characteristics, expected_type=type_hints["characteristics"])
            check_type(argname="argument counting_expression", value=counting_expression, expected_type=type_hints["counting_expression"])
            check_type(argname="argument mitigation_timeout", value=mitigation_timeout, expected_type=type_hints["mitigation_timeout"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument requests_per_period", value=requests_per_period, expected_type=type_hints["requests_per_period"])
            check_type(argname="argument requests_to_origin", value=requests_to_origin, expected_type=type_hints["requests_to_origin"])
            check_type(argname="argument score_per_period", value=score_per_period, expected_type=type_hints["score_per_period"])
            check_type(argname="argument score_response_header_name", value=score_response_header_name, expected_type=type_hints["score_response_header_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if characteristics is not None:
            self._values["characteristics"] = characteristics
        if counting_expression is not None:
            self._values["counting_expression"] = counting_expression
        if mitigation_timeout is not None:
            self._values["mitigation_timeout"] = mitigation_timeout
        if period is not None:
            self._values["period"] = period
        if requests_per_period is not None:
            self._values["requests_per_period"] = requests_per_period
        if requests_to_origin is not None:
            self._values["requests_to_origin"] = requests_to_origin
        if score_per_period is not None:
            self._values["score_per_period"] = score_per_period
        if score_response_header_name is not None:
            self._values["score_response_header_name"] = score_response_header_name

    @builtins.property
    def characteristics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of parameters that define how Cloudflare tracks the request rate for this rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#characteristics Ruleset#characteristics}
        '''
        result = self._values.get("characteristics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def counting_expression(self) -> typing.Optional[builtins.str]:
        '''Criteria for counting HTTP requests to trigger the Rate Limiting action.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#counting_expression Ruleset#counting_expression}
        '''
        result = self._values.get("counting_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mitigation_timeout(self) -> typing.Optional[jsii.Number]:
        '''Once the request rate is reached, the Rate Limiting rule blocks further requests for the period of time defined in this field.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#mitigation_timeout Ruleset#mitigation_timeout}
        '''
        result = self._values.get("mitigation_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period of time to consider (in seconds) when evaluating the request rate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#period Ruleset#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests_per_period(self) -> typing.Optional[jsii.Number]:
        '''The number of requests over the period of time that will trigger the Rate Limiting rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#requests_per_period Ruleset#requests_per_period}
        '''
        result = self._values.get("requests_per_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests_to_origin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to include requests to origin within the Rate Limiting count.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#requests_to_origin Ruleset#requests_to_origin}
        '''
        result = self._values.get("requests_to_origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def score_per_period(self) -> typing.Optional[jsii.Number]:
        '''The maximum aggregate score over the period of time that will trigger Rate Limiting rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_per_period Ruleset#score_per_period}
        '''
        result = self._values.get("score_per_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def score_response_header_name(self) -> typing.Optional[builtins.str]:
        '''Name of HTTP header in the response, set by the origin server, with the score for the current request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/ruleset#score_response_header_name Ruleset#score_response_header_name}
        '''
        result = self._values.get("score_response_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesRatelimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesRatelimitList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesRatelimitList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ed52014a7b40a4311f2ffdac2a7391b549d2e4ef55fad79a67e0d841732981)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RulesetRulesRatelimitOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a3748e04283904431acf3f1fea20683b207ce02eb7b81f9bbecc35d7826b36)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesRatelimitOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd04c0ed2f10d167ad2df21735c239b6dc0a3c50da18d3c65b7f63afe14e60e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84c77c1786df91710e3c705f3e0512ca3ea0f0c04df3d50d42004b402ecb61ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d960f42ec6b1275b6e5fd9318fa586745d98a49b86f867a76942f66b78b35f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesRatelimit]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesRatelimit]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesRatelimit]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71bed2cb577dc3e51ca6484851e2594cfe57f0ce68f21d0d943189cd6ba51554)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RulesetRulesRatelimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesRatelimitOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c616591c8da5a491380cdf450e548e21031b87e9294646f85449ca6876de3b59)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCharacteristics")
    def reset_characteristics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCharacteristics", []))

    @jsii.member(jsii_name="resetCountingExpression")
    def reset_counting_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountingExpression", []))

    @jsii.member(jsii_name="resetMitigationTimeout")
    def reset_mitigation_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMitigationTimeout", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetRequestsPerPeriod")
    def reset_requests_per_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsPerPeriod", []))

    @jsii.member(jsii_name="resetRequestsToOrigin")
    def reset_requests_to_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsToOrigin", []))

    @jsii.member(jsii_name="resetScorePerPeriod")
    def reset_score_per_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScorePerPeriod", []))

    @jsii.member(jsii_name="resetScoreResponseHeaderName")
    def reset_score_response_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoreResponseHeaderName", []))

    @builtins.property
    @jsii.member(jsii_name="characteristicsInput")
    def characteristics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "characteristicsInput"))

    @builtins.property
    @jsii.member(jsii_name="countingExpressionInput")
    def counting_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countingExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="mitigationTimeoutInput")
    def mitigation_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mitigationTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerPeriodInput")
    def requests_per_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestsPerPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsToOriginInput")
    def requests_to_origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requestsToOriginInput"))

    @builtins.property
    @jsii.member(jsii_name="scorePerPeriodInput")
    def score_per_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scorePerPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="scoreResponseHeaderNameInput")
    def score_response_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scoreResponseHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="characteristics")
    def characteristics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "characteristics"))

    @characteristics.setter
    def characteristics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b0cd48e1ff7c508e618a16911b45ce274e1ffa1e9b477882d96de1d6657118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "characteristics", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="countingExpression")
    def counting_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countingExpression"))

    @counting_expression.setter
    def counting_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2562c7127d2dfa33fefd0f6bffde74b783643c9d8d13d33c50f91cfd3c0265)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countingExpression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mitigationTimeout")
    def mitigation_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mitigationTimeout"))

    @mitigation_timeout.setter
    def mitigation_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52721aa2d2a6c39fa5cf18c5be98c7ab022440a4a608d2d192c169ac6ffbbb96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mitigationTimeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb40c77672534d59de8ef1ca7aa3bec4e1cfe1e8582845e31280adf823c8a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestsPerPeriod")
    def requests_per_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestsPerPeriod"))

    @requests_per_period.setter
    def requests_per_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59eeef774c6a88cd0adcc2d1a084d51cf25eaa2d723e8ccd646573900edbee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestsToOrigin")
    def requests_to_origin(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requestsToOrigin"))

    @requests_to_origin.setter
    def requests_to_origin(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b863854fabfaf4e822152022ad0a713953d1e8f06320a7ec6553135b0ee6f08d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsToOrigin", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scorePerPeriod")
    def score_per_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scorePerPeriod"))

    @score_per_period.setter
    def score_per_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f564e8f18061972b7dd3664a4835038d5fa7ab965351ddebe57ebbed7ae50b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scorePerPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scoreResponseHeaderName")
    def score_response_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scoreResponseHeaderName"))

    @score_response_header_name.setter
    def score_response_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84df3339578e8903f2849e365c7e2772c60aa07c8630705fe9eb977c8b7e05a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoreResponseHeaderName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesRatelimit]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesRatelimit]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesRatelimit]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57f640f30ff5cf10d412277ad7c65dbd58dd9da5260bea32529a5d8f1192980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Ruleset",
    "RulesetConfig",
    "RulesetRules",
    "RulesetRulesActionParameters",
    "RulesetRulesActionParametersAlgorithms",
    "RulesetRulesActionParametersAlgorithmsList",
    "RulesetRulesActionParametersAlgorithmsOutputReference",
    "RulesetRulesActionParametersAutominify",
    "RulesetRulesActionParametersAutominifyList",
    "RulesetRulesActionParametersAutominifyOutputReference",
    "RulesetRulesActionParametersBrowserTtl",
    "RulesetRulesActionParametersBrowserTtlList",
    "RulesetRulesActionParametersBrowserTtlOutputReference",
    "RulesetRulesActionParametersCacheKey",
    "RulesetRulesActionParametersCacheKeyCustomKey",
    "RulesetRulesActionParametersCacheKeyCustomKeyCookie",
    "RulesetRulesActionParametersCacheKeyCustomKeyCookieList",
    "RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyHeader",
    "RulesetRulesActionParametersCacheKeyCustomKeyHeaderList",
    "RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyHost",
    "RulesetRulesActionParametersCacheKeyCustomKeyHostList",
    "RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyList",
    "RulesetRulesActionParametersCacheKeyCustomKeyOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyQueryString",
    "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringList",
    "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyUser",
    "RulesetRulesActionParametersCacheKeyCustomKeyUserList",
    "RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference",
    "RulesetRulesActionParametersCacheKeyList",
    "RulesetRulesActionParametersCacheKeyOutputReference",
    "RulesetRulesActionParametersCacheReserve",
    "RulesetRulesActionParametersCacheReserveList",
    "RulesetRulesActionParametersCacheReserveOutputReference",
    "RulesetRulesActionParametersEdgeTtl",
    "RulesetRulesActionParametersEdgeTtlList",
    "RulesetRulesActionParametersEdgeTtlOutputReference",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtl",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlList",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference",
    "RulesetRulesActionParametersFromListStruct",
    "RulesetRulesActionParametersFromListStructList",
    "RulesetRulesActionParametersFromListStructOutputReference",
    "RulesetRulesActionParametersFromValue",
    "RulesetRulesActionParametersFromValueList",
    "RulesetRulesActionParametersFromValueOutputReference",
    "RulesetRulesActionParametersFromValueTargetUrl",
    "RulesetRulesActionParametersFromValueTargetUrlList",
    "RulesetRulesActionParametersFromValueTargetUrlOutputReference",
    "RulesetRulesActionParametersHeaders",
    "RulesetRulesActionParametersHeadersList",
    "RulesetRulesActionParametersHeadersOutputReference",
    "RulesetRulesActionParametersList",
    "RulesetRulesActionParametersMatchedData",
    "RulesetRulesActionParametersMatchedDataList",
    "RulesetRulesActionParametersMatchedDataOutputReference",
    "RulesetRulesActionParametersOrigin",
    "RulesetRulesActionParametersOriginList",
    "RulesetRulesActionParametersOriginOutputReference",
    "RulesetRulesActionParametersOutputReference",
    "RulesetRulesActionParametersOverrides",
    "RulesetRulesActionParametersOverridesCategories",
    "RulesetRulesActionParametersOverridesCategoriesList",
    "RulesetRulesActionParametersOverridesCategoriesOutputReference",
    "RulesetRulesActionParametersOverridesList",
    "RulesetRulesActionParametersOverridesOutputReference",
    "RulesetRulesActionParametersOverridesRules",
    "RulesetRulesActionParametersOverridesRulesList",
    "RulesetRulesActionParametersOverridesRulesOutputReference",
    "RulesetRulesActionParametersResponse",
    "RulesetRulesActionParametersResponseList",
    "RulesetRulesActionParametersResponseOutputReference",
    "RulesetRulesActionParametersServeStale",
    "RulesetRulesActionParametersServeStaleList",
    "RulesetRulesActionParametersServeStaleOutputReference",
    "RulesetRulesActionParametersSni",
    "RulesetRulesActionParametersSniList",
    "RulesetRulesActionParametersSniOutputReference",
    "RulesetRulesActionParametersUri",
    "RulesetRulesActionParametersUriList",
    "RulesetRulesActionParametersUriOutputReference",
    "RulesetRulesActionParametersUriPath",
    "RulesetRulesActionParametersUriPathList",
    "RulesetRulesActionParametersUriPathOutputReference",
    "RulesetRulesActionParametersUriQuery",
    "RulesetRulesActionParametersUriQueryList",
    "RulesetRulesActionParametersUriQueryOutputReference",
    "RulesetRulesExposedCredentialCheck",
    "RulesetRulesExposedCredentialCheckList",
    "RulesetRulesExposedCredentialCheckOutputReference",
    "RulesetRulesList",
    "RulesetRulesLogging",
    "RulesetRulesLoggingList",
    "RulesetRulesLoggingOutputReference",
    "RulesetRulesOutputReference",
    "RulesetRulesRatelimit",
    "RulesetRulesRatelimitList",
    "RulesetRulesRatelimitOutputReference",
]

publication.publish()

def _typecheckingstub__976786290c680465b7503207e2760a89b7faab8f545d61010c5b231f989d5e9a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    kind: builtins.str,
    name: builtins.str,
    phase: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    zone_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9220a4ee626fa5b46efa9b641bf2923cc2fc05444a070651e7d2338b99871c5f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881837c538b68bfed772ddae8847420413bdbc447c99cff9d5a54a1e04334cda(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e80fb2673b8f294f1f67700c48de5631ba9d9c567cb81cb7c00d7163b475a0d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5dea1392d141168a91b4bd2001493954d20c1ea1a06814fdf6869dc5f96bfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3350d0df37447458b9f40b63bffd161a6dcb0c965ebd5a4ae057b97f5cea4d12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e821cae1ccdf5e020c021afe5d57e5d2a88a5d524b4ba61ad522d8842625cfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bad56699a9f7b700c704be44e1189db8b97da2bf789aafdc922b8e8e400427(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f15432da9ba29f74d3ef770a089c57008555d54590ae3e98cc690d0ba5f956b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c5cd7dc19dc7eb2bb1a771ec52756f2b48fb9dffe752e856e8e778bd43737a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kind: builtins.str,
    name: builtins.str,
    phase: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cca2253f99d951ccb4d27f919867272a1d49d30084abd0aa98f9315a79b791da(
    *,
    expression: builtins.str,
    action: typing.Optional[builtins.str] = None,
    action_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    exposed_credential_check: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesExposedCredentialCheck, typing.Dict[builtins.str, typing.Any]]]]] = None,
    logging: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesLogging, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ratelimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesRatelimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ref: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d6b0152ba2e2b3e20a1543e04b3a6086c9466575dc6ccbbeb755c66c3a0f146(
    *,
    additional_cacheable_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    algorithms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAlgorithms, typing.Dict[builtins.str, typing.Any]]]]] = None,
    automatic_https_rewrites: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    autominify: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAutominify, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    browser_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersBrowserTtl, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cache_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cache_reserve: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheReserve, typing.Dict[builtins.str, typing.Any]]]]] = None,
    content: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    cookie_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    disable_apps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_railgun: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_rum: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_zaraz: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    edge_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtl, typing.Dict[builtins.str, typing.Any]]]]] = None,
    email_obfuscation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fonts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    from_list: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromListStruct, typing.Dict[builtins.str, typing.Any]]]]] = None,
    from_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
    headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    host_header: typing.Optional[builtins.str] = None,
    hotlink_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    increment: typing.Optional[jsii.Number] = None,
    matched_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersMatchedData, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mirage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    opportunistic_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    origin: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOrigin, typing.Dict[builtins.str, typing.Any]]]]] = None,
    origin_cache_control: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    origin_error_page_passthru: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    overrides: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverrides, typing.Dict[builtins.str, typing.Any]]]]] = None,
    phases: typing.Optional[typing.Sequence[builtins.str]] = None,
    polish: typing.Optional[builtins.str] = None,
    products: typing.Optional[typing.Sequence[builtins.str]] = None,
    read_timeout: typing.Optional[jsii.Number] = None,
    request_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    respect_strong_etags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersResponse, typing.Dict[builtins.str, typing.Any]]]]] = None,
    response_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    rocket_loader: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rules: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ruleset: typing.Optional[builtins.str] = None,
    rulesets: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_level: typing.Optional[builtins.str] = None,
    server_side_excludes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    serve_stale: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersServeStale, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sni: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersSni, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ssl: typing.Optional[builtins.str] = None,
    status_code: typing.Optional[jsii.Number] = None,
    sxg: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    uri: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUri, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e0262db6c09550d44d4c025ce790ddd6d039f1166034a90a652c14970d71f0(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab76d3bcacbae8dbd6d7d039f95a5b1951428d72e784d198e61ca5103b09cb5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1451c3add3e56fdb117a400066b42fd2cdec02a34bb9780d2682fd72f28926bb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb28cfe914ce1a99927f2b582f58cf638aa08351db03b87d9d87012c73f63380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e44bdf5c2a6eaa4c2d73a245413b3f39f4c9df40c77dfd1d3574f1b662c92c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8896d4d9b26233a122db109114d50563519397456323b2b07f1627653f8ceede(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9217775ff19fe799a909d4e61c10296b4d72735af343ba953508c8d86ae6cf7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAlgorithms]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f250fa9a8f3a9ebfab37548a40a5793a53a1e88a09e9970ccc65e6e9259c44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a1b6f08425a7b315a07742c073c033e7548e5d0659bb92db1eb99459e22365(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4531dfdbd831c864773006b1406d7157fa4a2ab3c94b3935a51ac7a0b7193cae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAlgorithms]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00900fd4560c9b2410c168ed6fd981a9672e97d2d001b9fa2a687f864db0e119(
    *,
    css: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    html: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    js: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7212c344c8c084ef7b27a7cdc3b3c6c87a75d5960c83fdd98ab354b44b29130e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a363f084aab67fe73e37f8b04d652cc76ef79592aabf569546cbc880987ac3e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b9a0a7420995e24dbb0ac0390152f22c6cc48a4871f180037b49cca423227b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c16e153a9587a76abd192d0be4ed2ca4e6de13c04f4f1cb7b7efaf729db71e4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a39560922b1326bfd90d8a55e817a5248bdfe721128b4be0e039e1e2d702239(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13867b203784083654161e3f10ad54f0779e23e3bcba05149830b7ee28f6e25d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859ebfff2651399a8ff0a9f49df2a4f6478db32f9fd5544ddcfc540e4cf5a9dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7066d2d93aa6d9388f0f368c6cc12befea1199d70139d434f089abd6c285cafe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c36832329b69f82c2fc23be23a95f5ea6bf8b9c38062fe9522aa275469f84cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dd89f47240bc2fc27119bbde218ceccf2902aa5b37e2eaedff2db2ae48c63b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972808188d2aefcf0e85e9f88bd170d2aaca612ec6fcb93884b4834c929c70b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersAutominify]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64155021267b0d4e14762908aa9c7fc518abf5d99cd0bf32b6a0d6b3c61693c6(
    *,
    mode: builtins.str,
    default: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7502e06ddedacb72a2014444a0b76a699761f4b69334238a699fe785bdfd5a4e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f4e30dbc8117add7273f12f3d239f6452ed8732c348db3959b06d552b0299f2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d437f31ace399c5c0f597176188a65277ffb0e8361acaabd1868542064dc52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12e9d5389461020470fc87ef5587d3e5e2b6140103d06d94a79a921dcf52b08b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b2cb1876ee02d13cee257ab25d2049be8bf31d41f6b078e18104c45f9295df(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c23889d06fa1cf6aed1d21a3fbf0a028fa173b359b8121e8b89d51960863c2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersBrowserTtl]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618e0e995f1c33f56cbd28afb0b26919c2a30a9fdb42628bc01383c9ee2ba9a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5c6b36d041498713a003ebb7246285cd2f1acf1a86c7aeb00aed655e611ad2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc9b0e8438bca2c5d989294321ac3fd033dd901359d03f77e9b545f1ffbdd5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9b571106342a360dccb3b6b33411324990211719353250ef910dba464ce20a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersBrowserTtl]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5dc4f1f552afa7683d5267005ed7456167729c51d25c824e9fba6195fe1c8b(
    *,
    cache_by_device_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cache_deception_armor: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    custom_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ignore_query_strings_order: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41c26b3bbdecd5b59a50b53991c15b99532af58107eb1051d8e0c59a03f3522(
    *,
    cookie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyCookie, typing.Dict[builtins.str, typing.Any]]]]] = None,
    header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHost, typing.Dict[builtins.str, typing.Any]]]]] = None,
    query_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyQueryString, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21036ad820adc9ecf2e54a6139026c938822ca8e16635180e68513d64e53112(
    *,
    check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93de0251987de35689d65ce443ab2228387dcc80ccaf02e035d186ecfcb092db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ac471c888453e2194de3aba8a0fdb92e23ad58ae3df815bc86de7fa440fc0d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e9c409a3aea876f100fdf3403f0f65469a8f16abf33cbc04c4b71e2357565f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17a44eceef8425038bf92c6a51312963d62100bfd3c96ef4eb6881404716359(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86cc45083e22dd050bc9bfcc5d916d3eedda93c2f59323593a86055cdd95847(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1baab91a494f0d69418d90eb8f2d036330211ca0e9eb66e68184dd38d498c974(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyCookie]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb0d96812e9e5dae46a3ca32ff3e21bc820473d8f677e46d83049000c4219f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf3ffe785d78da5a3110b29424cfd439b8bfa9df5c34c242be2fd4cd4e95dd8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537ff1156b88f89b7234398ff7bb2b3f14709a2266eb67cf78c0fe596db42d18(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7720c5dab1bff1d3bc87be21df59916d787fad17806baa9a624aca8b24dfee5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyCookie]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5736cf4f272699136c8f912f9c796dd3759d9bceacaf833672b0b527a785e9d(
    *,
    check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
    contains: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
    exclude_origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe13ae59c7bded6757aae25a012e8e7ba0787c156461c3e346e0cf246fa46819(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83ee8de63ae449216f78872986cb87635781b8cfdb65b3a1ac8914058026c7d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25707e45d5604174906e739421cfb03d5b3a86ca7c37b73190d98b93ab16e528(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85feea8dcee35eab665cce2f4914c1c2f77ead9e2268f3fe3b22c46fca8763b8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d07ad3fbd9415a2aee0aace1a5fd85b5a820341eed5335cd3aded196da3ab7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e64d7b56a3bf46b8eedfcb9f889c66189e8fee40f101c7c1aba3ee8ef2e1d2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572c1c886983afb6c5088c782e9999218d206f6c94de79704997c04a20798b49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76d37c74d0200150e44a0d00a759e21a645b9da99f2200fb5ed676750ef0ed8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c63441fad8ce42badc7990b9d3d2921ad2e1947861d8ea2f6f72fb1407dbc514(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Mapping[builtins.str, typing.List[builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__099d77f63dcc5d9e03581c4ea12ad3e4df8c15e0d705c49e3cf2159fb950fb13(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c038ed08b946ce1ba9d3cd8c177d1d5712953b5613bbb02f22e5e3ed46e0c3e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c561e0ed3436a5035fef2a0947bf09385708368c401ba65b2aa395b05326e884(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHeader]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172655455e537081c566b2ab3b5a9e353c1b3ffcc4ac8f47dd43e22a2026ec15(
    *,
    resolved: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910cf0aecfc13fef55616c107dcb604bb99e0f8ac49067ba2df9fcbb0c4fc1af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13244f99723fb749545930598af63110908b9b6ab2e222b19b6d0420880c0e6b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa37648d04bc631e00f0abfa176554dfde489c03ad80352b449c6eb4a253553(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d193fb023323a8e8c02d6e91151c6a439a1326654aa27da466230b8b22d182(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9140cc7eeb6ce4732ed3dcc2150f4de68cc71620e02da38bb3e726559f2b229(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfacb13d0c4ae8de37219e62e4da6bbc0099b163e8b0a650a83fa5663c07c29f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyHost]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cab141b386661b5f82059c12be685445b2c72626547bbd0a6e335ea2a2042cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b21686a047e96b688dd7e438de047c689a9bcb443e2535de17dc5039d4d1247(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1206431d417cd671814597583ac30781b1d4c12674b8ce0756268127ad087011(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyHost]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f20eeb11f492c38f80070899ea81529d2c83f8ad1a82f716007068b15c2437(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1dcc286802fb640ce3de13e3eea795a849c11e263219572b7033aab6db432ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16999b302d6a4530dad1116969d675d022b6eaf8bb4faa249b84f7546599904f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68a85f4c3bc632ff6f6b50a349e68968e919c7e92434ddafddd4353ea645cc5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8d6c5fec5d15090a0c66ab1461c5f40aac2a8876159e99e3b07ec6ad6151ae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa3c96ccc2f11908575a9d6318744e897fac20bb51a4ec90985d3c79bc6547b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3e9c0d9998ae16667369b9969dbb9669968802cedb705b719a998fcc8e7e25(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac138deeb48fa0d5738e9c6fa9b11d51b6411ed75951dfaf0a28680c9ffac9a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyCookie, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f761fd3d74609ee17cf205b3d46e784975328cec019a7a574a3ec77fff459c5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a8287ef153780193a8eb807894afeb92bc77579645952d407b021cb0ea1a64(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHost, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e968a38de883b5388e3e4364c01639f6ade5ecc7210c3ce8188b8fbf737141(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyQueryString, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd7a4858c06821c37ced77eb072525c4457cb2434985ed0aa909fee3b8a953e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea3644371990a184e17695faceb338d641678396fcfe966d9e151a71a233215(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKey]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7b4285fd61de06c6ee33a490a292729c0bbe60c2c265b6db5eea8da223f67a(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f2558eadf7ebeb6d1f261a53174043fe5ae00eb5e4cf36430fc56090620b83(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dac35c4dce316f9795d8cce8485dfbfe163e0646f4ddfd83a2c18f9d340dfd0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad34e64a2cf2bbf940aade76f3b3bcdbbf2604b15470670c70cc62b4bb641e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef93d9259b21a757be5b299cd07c0d3167151e131e5fd5b5ae792c2f45c2da2e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5cf6a58f0b4358533b719030ba3787d21d71964fa5a2274fb9decae188e82f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3371c5b4ed76dab28a448c4b961601796d3f9d89e3c74541b2bb0e0e0a5bd11d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyQueryString]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3c93b34094c2b75e4b99f9670bad451c73e6bbd510673419efbdf0395ee4e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0da3a55291f064fdb5faba25fa71b0b7fe575dfeb35315939174070bc5a0ec(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f683aa3c6de4602169f3a050011d700e570eed5446d978bf4d156bb97984e4d3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df7aac92d496eb8e393664433b150825479f1ab67fcbb375b8b2b06f786b3fc1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyQueryString]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e924452562758bc0029e3f097ee591730962722f9415cbdae62ad5c99312a6(
    *,
    device_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    geo: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    lang: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593689f789b8f6b8a98b7268ef71cef873aa5f9137fc7e1e575e1ab408c025b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8470744f3b156a3a8f8e42851b8c735f204cdd3d5b2a33874a1d6514d25af3e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__875dbc081643c98f7cd387df5f4d886ce4954f694bea37b1a257cefdc7b744b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b33560c1b67f255789ca6b7bf80e494ac4991128764dd23dc199b491deee05d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2120e46eb10538e254daaa06cc920c52c779db84abc9c971bda3db666a7f60a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c830910c74b026710062a65e2197b789478c76f820d0f335917460b90b1d8a48(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKeyCustomKeyUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54755d8b6a77713d1f599449b00c107d0606ce8da84a3089e41ea527a32979f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__118e87128a54c0a6a808884398111aa7d7e42619ac2998ed9c7994149a2e673c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ec499284751ea78350e508a3abcbcb5d358f36ea55633d83cd7544ecfcd8f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__649cabf797e6afb01eb8f703947d9cfd1d2f6e8e6124fa69fce18fc09c189c90(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9927298f8b3d3447fe8f48459da6d6a83934967c742bb540bf20da76127120a6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKeyCustomKeyUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b01ba3453b6c20ef499fced682b50f9740f78c2596db43329ac5b81996672c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e50a4885609bc6b6e71c8fa3b69fe38530df6d19d3d40bd025dc6eb10f548b17(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c5c89fa17d8ea711f302e0fd81dc9d4c066942a9a00d6e00356a7e288a714b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c5943ef13104c0a358cf5fb7fc13c3f07b65c0931de99c118984b8fc048836(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc93b2a9d8f6c6ebc157d2d06e31278aa114c6b44527772d47a1857ffe70cd7c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772e60af4421c33a856fdd865196555f4058c09ca10a6a020405ad4c82d42153(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b8429f9631c7f4e81e16a71bc7d2ba9e3a4a61fec48eeea0f1e6eff39efd34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdfdbf8a49fcc502d1c98a4ecc2eac53348f32515527b9e9b76e44a9f7a0cd2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKeyCustomKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7008c0f9237f3579ed64d4615be741d342fa0810924e2ab328fdfc511bea72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cbc18ad859c2e5194b72377e26f9d1168619a5982b43b3364bc18606b92f870(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d70ccbb43451c8e3713800708a04ab330bfdac22e4e81e3ff7f152a6ad9077(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5e95b07849f4be277ce84da62fec0c34d592a229699ce2c8ff002136fac1e4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheKey]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb239771d4009aed0c39f9f48bbed27aa2d69cfe4ad90ba4e2f0f2edf518b2a3(
    *,
    eligible: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    minimum_file_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8445055a29da7a38852fa1ab9b21c675888a8c6e8c9b571b8ff055058241c699(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cce0377fbcad472143a3a282d94881af9fabe86e9d06dc4189de62a12b4de4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48271d120498cf0035319f9841b704a6711ed031daaac1f0a19f3f56fd1f3e21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77aec4e48ff9ce8f9ba2735a335684e837764aa4c0b8a84f641fe76fc7b6e6d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af703b933f54dcf6e920e7116f0191bdd7cc48baf923706e41c70bc79300408(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd07171c652766038cc4a10e92ad7d04390bbbfdb33ba8f9346a5c819973b5c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersCacheReserve]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83846cb6c021d54cae085d576ebf881b257d4710c2a21c7bbf1cb2a863df2730(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50fc546e11eb198d4c672f0e18d9634f12bfb8b1f8e5af296aaf0cd779374723(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2393a403b9e110ef3fe0dc538beebabf227c07e9e5a4c04b1a1ed6cd664c9769(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c172960cf40cacaf939cd31c3e19373dad237d9be2d4abc42711c8d2ef26f55d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersCacheReserve]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2adbcf077256eea528469fe51105b233df404214ccaeca6a85e07946e6a0d1a(
    *,
    mode: builtins.str,
    default: typing.Optional[jsii.Number] = None,
    status_code_ttl: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e99dabe5822010205510f1e95095bc12a24e3eda5939ae518b0ad06a1f1433e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f67a9aae03da6be6f4fa39595fe245c806fe408cacccb946c75436bb94d1b5a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d43ee02c025cec0da804e9254c0fb5ffe8d78978e2bcc389e05069a8c3c8ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c940e258b9eecdd8954a0938ebb7d5edc937a78624d8599ddd0789268000a970(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb5305398f8126a5dfdce28e14789079305ed85b4d805bee88c58482ba1bc39(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753b5b7f30b1fdfd74881fd6768da28679557a329a222c0d42729fd9b4e2491a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtl]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d26af6f6e3836ca45f2f660b7f6fc6e440a5708bc24173a2f9a9b93e521909(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5898aed30519c65916f3516e03b0c5b2a482618fbb99ff8eed8692e10109f38(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca1b9a6f1a714476b55bd9b153038e933b01ae1e9de408b86c1bf1638079064(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d4345630e346df22f1e89d154dde919e4502eebb8e88265688414f0a2626cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2050d59e7b65ed514e7e5062fc10e07e175a5a72a4a676658d4a61742216c145(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtl]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3673fa2048e013a4a46d6ac26004801528dda62f81db6c2fa68f68e01e0e6605(
    *,
    status_code: typing.Optional[jsii.Number] = None,
    status_code_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba6f59140aebf5b4e01a4909e04a155d21689935bed3a5bf7fe8bf2cb172c6de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5843232fdc4262447b546bd8656f2b9ed6644c356c348f236ce488e742c19422(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097d1b4ef1a297f0eefb68f409edb861d1a8cde46543feda4611b83b979b8424(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c81f7217d11e61fc2a9db0de37ad26efa084c3f3cd7f47d464d5c57af1996b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4610355139bcea4c6748dcb306da92e33ad66b1f47ac0bbab3f8917d72ae58c5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37eeb71739e6dd95fbedb9551cf3217e66c0e88fcf675c98f35c89376a6a3de5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08afdb74723920f7da0de5c614b150aa3088a3701db265eca5a162a255a9a98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5243b09455914f0120eb29dd6eb000de5bf20fc7a9d63f3fb5d478a1481c818(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980ec2945afc28a2effc73cc55fc03e92f12feb6ec75e13e6a35fc6420b210cf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b95217c7f7c8ad8bc9127cbd39ad24b346025d33d55d6c1133a144242062ef(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63905ff61e4ef02f2c86e426d9de5bcee56988e80e3cb5c2fd68cdb775f2e51(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtl]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a25235665711c4041ce37b303e51598ad26898a434cc3160e4917eecb8ef7b(
    *,
    from_: typing.Optional[jsii.Number] = None,
    to: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__040a8a88ebb01a29492392c17126b54eea1ea94afc74ff97913ce0dbdf294767(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9472aa688b2900ff5dbd9336e12ac006c9f95fb4c2cf7e8419663ace930474df(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6154090fcb398a6c323daac743800e63ca2d2a8fbf1eb9a6b5a66302ae83abac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f40a2d416012b5cfdf4b7020fa1687c80ed9a93f86666057e51b59b23dee7b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743c87b95a0b9c57cffd8871e4d5a803027bfeeb5e1e77479066bfea4e7e2529(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee21671353a5b3b96ac92ad182d8a08ac585883230482b75b76a0b170ba008e6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc2e4b4c701b4f62c3d3e1af53d1d6346d822b38d7e7ac1cd0fa012491fc944(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e3afbf86ba5f2b22b890fb6422ab6bb7a12c012c2415abf31ae2ca5e246fa6c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1698a22751a5220477692ed03bb293b1cfa2534c0e9729f13df8b09be13c2bb8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ccd858829d1059e0b6f536c3fb04871be3b7ca1dadb6167ed1b45eca02a7efb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b67297e45830ba9e9e493dc7bfae4e3f7f64c4196d83dfe3bfcc5bb28b4b507(
    *,
    key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c70b4dedaa910db647d1f9addebc1e5dd138003a9112dda81235689081d26d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ebaeb0283c3ee7b7722699a88fc3db518690e353bee97bfff8abd3e39bed2c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c308d650bd04f850182eaadb8efe3a78c86d53860da0bfcdfb3338663a91b824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c800838c4e46849d084c83e3b2de1ac0e1230488ef3532ee6f3702154fdc28ef(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a05634e13bf31c84ce334ee20506c2dabbf15a48ddfd3003480eef2bdeac5d02(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da4f3a9a1e2ec52a5bf1492801389733065b3a643724ab55363f66c2f60337c4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromListStruct]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ad50478c51ebfe851a1202f0eee561e58ac9c8d5ac9f9dd845445be7d27095(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc57cee4e4d328d61e69700340a43b873375e6fd941a218084660ea69230e2e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904a219d759fb3dd4fbb6cbdaf10fde17cd05747e9712f93eb196ba2d494fcdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e569509f78948c3b20e7351605121e529c164557e790879d1bfc357deb39ef1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromListStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b617685cddbd9ff58e47258970e6023730c625e0d17d160b4bc521fea77e88(
    *,
    preserve_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    status_code: typing.Optional[jsii.Number] = None,
    target_url: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromValueTargetUrl, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30bef636aae2dd330b55ce293888f5e6ce57e738acc7f9d74f824ec974c2e65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25a97d48e0beb53f6e5943adad5e01abe957af29ba3b866ce81dfb0cedc41b3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6173b7480ff7497bcb2b857b117b8f18ba74f6388a18a790aa194fd00399235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80fc1c8b77efe450d39b59e8ee2351e201384a7c902fe2f7e7ff31009a1d3f1a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71064ce6fb285eb20bb40e5a41e5bb973813ec288900eb962921e1ca2fa04ce(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c35341bbc5554ba31bf595eab6a01b1b4157e05a74c3f1b5570bc23d9afde2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14bfcc9e7facb7af52daa289700b5fc68804c2bb13e920e75cea840d3b11b0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e09462c0a00668ad50264267e33e4c499985a1a05c944d58291f14d842027b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromValueTargetUrl, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442bab0415161d2c44f7b4a8f57cc53c0ebb063a2d7ca08364042c29a4896e14(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c246ee97ca8b910ef616470f8d160ef0d00fd420db6b68d517088664670d6026(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb247ab659e2fbaf89fa2a257186f1bec68b5cf2c6fa4761bd9d050c347c2a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02bd6ce7e2bfcb866a45913cbaf053071a80f5319b55ca46771f3e7db50fd167(
    *,
    expression: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28bfd24702742ec150e14e6094196d9f8c8eeb0aaa14efe9d6645c0b9a0b4168(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57772fddb4ba4abfce84fdc378cf1f3abf373ee1c9579255611b9eacbb4d23e1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d7dc57ee3086bf96292c9ccbe19be26a3c74699c1cfac682272f72ee92dc9b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719ce08bdd959f10cbff26c8414ab42d1b464d0885667531a55e12fe0010c5fd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a6d878e0bc78932ff50d7a062152eb88bda71a79893f5f88e5a0942d24ae1b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9296ed72de38c1dbb3a7cba9fe44e54d0445e26c2a2683f5814275259427657e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersFromValueTargetUrl]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c4252337abab2e0099a3ad31e7175f65f58f06fb6590b6f9f8553cec9345fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4534868c475de22c561632b0d8e024ebb69e1aa7725e25fda4a979228e80457e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41518c81dc91a8969ddd1b9af70402b5dc007c626f7b933766f981c088a0a86c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913ba6418e4bc925f63b590b04b1a7cb716e01f738a10685f09bf63982b2e7c5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersFromValueTargetUrl]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9652b0b730f90edd91411f20b54239e14e14ff06dfc563f9f61e3a16b6c048(
    *,
    expression: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b8d4da10e304c7f89199d5211474b4c651342e5f5b9ff3803b37c9b64c5d1ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299fcca6fe4873c00ab6794bb6b10aad87b575f6f9d9b2f50391cb1101792070(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc9531dedfa7905814b7cb90d7299d5ea25a1c2ebc8041d021398ae2694711f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064db88945a642179712db631f02bd779d5a3340a7f89784a34c155fa6448ab3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba7b0ed17ce15bfbcf785f2a71c7fe4a6bae38e9e5c056578a79043bc965b78(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939291c9079aaaff2564e65706c33760d7f74110dc6497567e42d9f73d6c256a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfacdf328fa2609ecd011de17a875188c7bafaa8bb1b8105e15fef25add34b1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d822d3d4435667164f8ded41e86d5eaf60d62b7a7eaf88bb32cc1a577611a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b108ca26ef5770c015de28b30b6426eb37c44a2d0d33fe7939b38605852f9da3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2588ff959f1b47df89bd43164ac4a93c851c4b6f618800d15502e7e671335444(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840a8ae1386a674b2471be5f3aedcd3c8d7b05284c75ac7ca593dca0dbf1b571(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8dab90cc37dec2cb13251cba8532102fa4c230c824aa25858ba19a577652c06(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersHeaders]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fab722cfa46a0a5e696b2d315e34e0439cbee15d40d884fb6d5c3fe8f92d78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726e7e6036ce6403a84e26955581dda67b111f473ba057ad31fdb4690421e961(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e012258b38d9ae121b559d84c7d1e4c1bd1c7386ca404b508e29e5395a2d3a89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed3b9146080004d928c3a56b95c0ed6d737078fcd652a66cb2dc27c11159654(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6849de5e327a7c1c88bbec20248113c141eba97b65c5e518eb5b395eea1986e9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8534cb92b7abffe1e93fc9c65e1cc98a2d21d6b8954eebd036e5060fed87defb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79d24480fd9fa655d9e35cea6778e368ef22b575957402a26c1ce56e67b78a5(
    *,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eca00da8071730d4011489c64266d9884fe24abbfd6607ac3d2ed01a5e2fa41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7684b7762ac064774bb2f9c1631432728a80d08f58ed73bde541cf6631c34d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15620bc3c76dd25262a3a05bb5455de97bb3349809ee6f28ebc6e9a87a009fe8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9d1a56694297e6b933d8a166933a5b9dcf26690f65f67b97a4cfeb13fa20fa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e0a5be466a7b77fc0fb78fd725b1a5f6e6a45a232a8a69f81d7f5b1ac7013a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ce39b0c59daf679cd7a1964f516c86a8a616a9db99975b8d908233b9338ab3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersMatchedData]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba186a9743494693779a9e41dd6a2b9d0a4a06edd39331ca226b8a283c9fc29d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeeae244ab63610c3b8e2d8d04684195e4c143626b564aaa8ad018a99b99077e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10459137af99ae34d414b273da7570a083799c03706021cc90528bb03dd4622(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersMatchedData]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538f5da67f00eda4fe4eee29f992b9343c58a3da7e13f4f9a7eb2b45e7640f08(
    *,
    host: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22510ec03ab1a4f34b5555e2f261bf7d62afd66106a6a83c84edc02c03422bfd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35350591ea0d047cb4f14172a81482f1ba021ca9b985fbd2fb49265363a2e2ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e72d426ebf637376a4f9a0306d8bf9350699137481684dc89132ef3fffdb87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439ca7ca3ad95ea1669474aa7555437678d1c4d4c77f652bd3c2d7195b6c2481(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41af885442abf9b95872c496b45047e70b7ffabfb92ed680f0c46f4aabf9170f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc110626641facc7ed95637134bee238f59c36f873b09913b771b723eb4ec725(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOrigin]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4834ab77b72906e58302c5d50fd0a4eca483b2ba55ab4149ca7bea453e1fd4a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146fcfc00aa700c091a6ff77222191f183182f60cc02c42931892d61288ec6c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7298adec8969ec5c380dd8fce19252739063f1d26ad76f4ab92c9c406edbf1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa92555cb9bd54c4a1adb3c18197cc7867b725494398451bf2f4a58d125f7b1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOrigin]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27dba44e1ea75e7aad0490ea79a278b382f6f2d89f9e284e704a7d57ff8ef774(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a20ca357c17361d0dcbe282dae4126a3d1ff2dca9643447637f85a4a2ede9e8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAlgorithms, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad0ec3e765a1241cf39527fcaca381777a6ee8fab3cffc68d06214b5df97cb1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAutominify, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3113fbc38cf58a3a15fc8c4132ab3fe8544adbb924cff02904a6e12952e50dd1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersBrowserTtl, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc63d1883c581902cf872c8e4dd6836f610a288a93e2128e6611914d876a0cbf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1965f62742adbfb5deb80f62900d442d215e5003c81b59a00319f8fde4de9995(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersCacheReserve, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7def56a1993f2605c58fb72c4db7d77b861300c3e5f873e46aa64bc5c17ee2ce(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtl, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a666e699f3d133ad31c8ea6908e1c22cc80be5de321583e261b7f20a4d34f4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromListStruct, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e44fc45a1cc019c1df5eea5c5f055dbdf11d92af7da734a4d70adfc7e52c710(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersFromValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a2a2268d65b8ff60992ee857ac3de2a16987bc0c7284905092fce377644b9f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersHeaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603288bbd298ec391c5808de9d06fbfc6ab941ff307a7bc4b84f59bf66368253(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersMatchedData, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e740b03ae9f87dca4fada4913eb258eb4b01753acd7faa0ba5dc9f8e501599(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOrigin, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4bd718a8ad74c3ff76fb5cd2a1e8f8d1d5bd28598240c0a44b113636a27ea1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverrides, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b6140a8d3f2484a1102294eb6d7aef3531dc7aa3af13eb5810f11ab855aea4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersResponse, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c7c3c714ed5ce09d76f9e1392a37fb89db2b5e0a5bb15d1ceb7a6590ac1c098(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersServeStale, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f678fc6b262e5a71a88172ccbfd657bd7624d422f6b03a72f272609b3e9a9b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersSni, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f059292c55548b70cd94812d9cb27adb8513559a07eb3b324024bbc7db27f9bd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUri, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c70c141d15e6fba80ff6d26b5b001fabb33613fc6be2fd64b660aa5ae6d25b(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b211a463ee99fcd38484a48f3c399af92c95e2fdacd72e31ec1c2077f40336(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5fa057d561e1e0e156c5d6ba189df1696b28d0050888930aa10ae456f477f76(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ee1f2c3423c8c27aff273783924f9a5166519128d5c5deb7e6ba9bc7479f22(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25acdb5536551121106a45692e244114bdae17ac486743727919ce60d39b4900(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b036f29847efe4a4d4dd3bd0fa7806cc6b72e5f0ef3daaca282b882371d845(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e72f6a3a3ede57b891a1a294a8aa05790786a930a0256f0de02a87a070b260(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b045f588396b62337e9e49757f4e4c1d0269dee5b84092a75857a34426f6ac07(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8ca79dfd28d97b02d00e46d25bc47d1b606ab2154bc40ec47ae9c618f76187(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a25df6053b939d833ef898cd9d3b6d593c9840137beb9df02aa8f17e270249(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0503c6462ca0cc885dbbf47627a5a892f70060ae9e22761f114ec9ed562cb1f4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de03fd0bea7959103ee49f66cffff9443af5f7b3decd178e38e7fefdf31dfd59(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b7bc956f570b3f71a8c0f6e021433f2bd67d97a20fb1f05b3e82e07b0b696d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595e4e501b488cd0a2a89462aaf3a1c0dafe61f0d852a707b0e7af252c518e65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd27419be9bd0141c30e599024e5f3a9bae37e3e0c5417630274afa6c7264f3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c36a64d1a2cda8b8450f543be75de2ecbb4ec96e8b5a48bb7e975a19d1189c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8725fab92f8c931508a4c990fb0030902d4b7f7c60321a25e6cf8ee81d57defd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef36b756b3e0b775cd19c59d56a5440998bbd7721f7617245ba2b02259c510a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad32a10d8350bf6127cbef96327b8784bffb7b967a347b3ba121a89e30d309d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212a8ecbec2867d18f7b02f1a46f0ef109870d85b245f1a361e78189600ae53b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8789c7f1457fcfaf3f4002826d68697627ab6ece207fe56f60822436f36eca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142a215c62758d408656d18d174b7f0412278d46902198af8ddc2d6a6fbbdb29(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3267a60274b1664f20a4b469facd3e81b98007c4557fe846a529c2e61eb9bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d1a161bdac9b62e2298ea5c9ee5b80797e01c6f30fb3034b7ab72847d4ccbe(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6a64fd066c8a5bfc912e2dd835a395e9a49a39fa9b73e54409cc062efc6918(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5ed38becf243013f7d4d12b323d06d1466f18c998f5b55ce963be740dcf893(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa25cb0d5eada83326490127860c9e87b5da028ee760d21605d133a1cf92f26c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40de264f8a38f541533927727562082f6ab023b0a555883efb014d146e84fb6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c3ca2d0ac3819e9ab928bf9fa162f6d5c8f190352e9937fd1eec12a3e07e7d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ccba8efdcccec9bef2204ee4a12cdfd4e7b8da209c81c4346a27cf1224eb871(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9387c1cb07b59d08ec8e60a890d22a4240518137d2ec84f52411c4e8d19f76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1744824af7da4382968436ab7387d37c00778fad30941f7f5adf39bbe54eef4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23571c327a3a608db8886935622d5deb109d7acc36016503e3c3ab32c93cd2ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f9dcfb6206b557a2796b90e02bcf869bc1138f101eceefdf962940441ad13db(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da6500381dedb9c95a466d072c2e57cd23d0444d02d98ab8ac63740e7962b7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be717b9be7fc1946d5d943892d1f46ea02c6140c3ae620d0fba2ab46aff00a87(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23836a04174f99cee04cc396ab3fa32231f2f7b0f4f463782757304a50cb0b25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a644324f3a0583755f6708bb7c316e8a126bd4a604f0950e0303d26cf3b3789(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParameters]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289b231a63801bfc94b417b219a571458a2f775e9df8435517ca5141004b90aa(
    *,
    action: typing.Optional[builtins.str] = None,
    categories: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesCategories, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sensitivity_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870a3e9613b3055d66a04e84190aa900e35ca00b4179c5f914b92b850ff0d78d(
    *,
    action: typing.Optional[builtins.str] = None,
    category: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb5d6d7c449a715de0d634766afeaf11ea29bd26183066a79f47e48a29283c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26dd08b921db6db4613fab63c27b1239a65774fa637f1e2faddc664c5826fbe7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c825eb95aab5218b959203ff797d71420b620da86966c7f60d29dbcb6bacc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913fbcb3ed99a8c4e13200e8400020909d32532901ba819ab6eba631ec73e26e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fa4407817774bdfaa7f1febc82d4ae1bd04203c05546046a8397def461ca00(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada2b6725872dbbea5aefde73064d3d4cd92ba613eaa5a54071545b2297fee54(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402f123ba7682883847c231fb72fd3f1ebefd584ed8452dd982abcb6cddad180(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06dd0e40b1bbbeb6ed1b838f84f8f022bcd0f6e25aa52d0f802317bceef9338(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286a0fb32ec1b6fb46ec53b9aa8821dafb847cc73662be6df854bbb9fa3d6511(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd740b3b216fccf1734a09f57bc3f8893e2a873f04312213b3ffb8767a2e3885(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd79b3b5f8aafd85e5a10caf3324fbe20cbd9cfa32db38492719881c59eff882(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesCategories]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad927ed30b4f4f6568a2db00510ef7da84e3c5ae5d00f6e2a33ecc1f7aedddc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e686bcdb5011c4eecba9d2c5153499ad18cb868617580b81ec872d61d830c174(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c91a5254034c6ec40dff67cb48b6c88bb221930a4c2ad5addb2c69ae61c0f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3b6d42b83ff9d2852798fc3f44f0384978e15d970b25905a990c3ff80bf8fa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bc1cca55c1cf767737e562e0a2345e44197f70ec6c939b61f7b1e101fcd94c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f330bbac42a4a96e19690215dd6ba16bf42e6ef4c448760822807bdb91816419(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverrides]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4a75bfebf22520c432fb864d164587dfc6629af51c741571d1cae0dc473891(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f91dbcb328e5fe67c74764d783254676c987ddc83f84e5d0f4250c0f2e7164(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesCategories, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49231c10b47845919778a3ff0cd8cb45e4ff12408921d44c284253f402792c32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3571bd1397f3f382e68340ab32ef7a523fced2352e8530cf59a4ddc325b4b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb3c647c13014dfca348295da7d04550c088169dc31c683d9021fc61602644e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ef3a813e5713623177c0367d964f6f28b2be05033a87466fa361a71fc3da89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c9c29a54937eeffd9bbffd7ee83cd758e4eb9821f76e4503355534c4010b52(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverrides]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d719fd0336c6ca82eeb45415fc6fb6c6e6baa00e20ad4c5194223a1ddb5772e6(
    *,
    action: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    score_threshold: typing.Optional[jsii.Number] = None,
    sensitivity_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01983b963396a95702e44122c05081ecf289f27203551a2d4aca8e0be5c1b36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f152a794bed77dc33c6a8d522be32f6240105918ff99cbf3539a3b8958d7e9e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0376d1f99cce300788c8a55376487982090f60faf371b146407d3adc33e98f7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46926039e7e4361be6e6ddf5b42573fba9694d6e77e75ac6dd6876041db61b9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd6f32d3e802d8787776f8358501880e6226c4774d9236922e1b8b0e4d83cdf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a015621ebad45cd200a387d33eaf9893c89c3d5eb8a5c208c37022fe5990ebe3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a94fced77c1118bfb0394614428707b6a1e5bc17a6a17a634d3b22cc647d7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd03cd7b8ae2161dcc516a76373f45d43c12d45a4fe4d12d854ece8771164810(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecfc2aa84edb5d0d5b7c7c50ed56b5daee3e9acadabc79ff642b4f84cb967ea6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f4e4b28eeeea751243819793b76580b5ea3c634903f942afacdd666f12bd3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4e6b9ada3086f9c3babd33bc6f4f5d7ac4a0ac56e75114687c38140d8ebba8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2e50085ddd09296f10dbc42f17467188e97e556d33d3dc45f2081dcb22573d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d61b1f50416d66569c28bd50db859969c72a731dbc51e960869bf8a7ef51688(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersOverridesRules]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8500309c03e45915aabd35e7391cff360150a44d7935ae6d114d7e712875932(
    *,
    content: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    status_code: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff9889f313565d9195aafbb295c205e8c17b1f1bb84c4226d033e2961776f4e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5959c7e9b061c8e66122a056752a0aceca71046c9bc887ce65bbebe9bfeba54d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7294e3563e074fad1699be7810162951a75e3fe366b0803812685cebbcbf071b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bbae99f322aba3a6071f68bd369dfa277e1d2ddd8bcc549269df1b650c1e742(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d954a427499852fe0c5c65ec93c4ce7b27fa7c7ea506c3233948bd3159762f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c6479bf7dc277023c2ec5cb54106423f052c751cde054a056badfea8a9ee4c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersResponse]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d828939b8540c63d20da5a88a1d11fe8a6b8ed5126a9828bb92e9e64387e5758(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf12fabbfc8ec3caa72fc5163fa719866864783fce5c7e83513165b9e8fed82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80dc442ad7b77f1f03f573a2afc17acd6a921bd2e28bac18b10bd3cdafd72600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b469c3a82ebd109abcbf69cd9a73d38bcfd4129e4c0dfa670b29cb5e4fcef24e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a03892bf374fe4ba6438d6b5241fd066e843add6b3029ccaf63d66e3d41761(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersResponse]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6af794003f1fe3b30a4b979ab5d9747ad2e604f15a44e341b1f9fc74ff80687(
    *,
    disable_stale_while_updating: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcda3679642af7e720ab9e7016ddbdec9a825a30383124f531eb53444cacde89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1762de37fe78b51512d10d47017c77824472412303df61120de92f01dd895e97(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418dbcc20e9b1d0a8711363262d1c782b28f475064baf64d02dfb65956e40b5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeabc0973390ed2fc1e8b9e3318aa2eb315bcff02dc348c29c24deb94a115b59(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7817663479b09bde25a77fd90ec8ab72375a5ae3538360df2be9fb0389fbf8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1f438c4b1134536ea853558e11f7004abed04014c7027cfac3d7dbe3c5a92f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersServeStale]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8e58da406be38d9a7a0f737278761b2c34664b670b7f429dfbd3b22119c596(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9edf835625c088bf50a4f8bc8f239e9b5a8a81302584f4efe0fab9547d1f9180(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86250fe3ceb4eeb3c4ed04c9bc38212c7c77f6f5d6fa904b714e2719a3384263(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersServeStale]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec0b9d1ca4750f04b5189f1e472b6d5829ff6c7b4d7d1320ecb693673f8995e7(
    *,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b1f07fd35aa64a6f5a804c503bdcd071e0253b370cf504c416b7365fb96ffd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2d244ece81677141f520c8c4f3b4538fec63b2fce5994f7adf2c06d3fa37a8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf0defe3b44330cfdcac9965d070f7efe4b4ef7a9f570d78bc22c352b7686a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704e0ed0bbae97988539648897dca4ddd2f77f83782ca985c7d63d39778eb274(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f80659f8de0bb2997720b146321dad67156b5f4bab77ea98086ff1c45b1a6b7c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d81ea933adf0ff4f7dd4f637710517268cd295d8e5d6288fdf5f5397c64152c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersSni]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b927797a5318e3fe56d152556b11869b432f4eff52ecb15a4725d4845cbafd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__decf557748c3f6266ab6417fc1ec5b87e698c3ecdc4e4837dbe7062d644f2d81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026a8ff5b9c8de71b3bfd70fbe23ee887cd28add0f0052d324449e2b1ccf6212(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersSni]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7637f849e9379913b2b8491c44cffba72ac1044fed31376469b3ffb819976c70(
    *,
    origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    path: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUriPath, typing.Dict[builtins.str, typing.Any]]]]] = None,
    query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUriQuery, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247df54c4f268d519dda0282d940a8e29346fb25b668c9c76d31499c0730d5b1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df20e935ca559c1a9973dd3be551b2cfbf1cfd05a3d007364c6fae84164278fb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa81845a820cf29589dea9dffc7a701d6e2f0136e81042e20a45464ebcd05fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4837fb9397023f8f441892a5b877eb2ee7e2bff8604106186ee8a8cf00afdc80(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94ebb647f93ab3a3f04f29a878b9abaa16a06d0308ed22597552ad83063d376(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac76a5ed7bc45921cc2c1991c3eff6d4cbc55a5c9934f1d9c31babdcac25176(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUri]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e144d3dff4777b08e8aeeb362733a5f87dbbbf25f2bd9b516614e2c80bc54f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a993610f47c8c4dff9c33c9aa9efa51ffdfbdecdb141484953edbe054da709(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUriPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f1ef2eff78798976148f9e1efaea462f2a904b3e27b92096bba5eb8cf58d39(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersUriQuery, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce0ce97f42c3949b13b7ae2c2c0cfb4123275b2e6862839847cad8711c399ff(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a4c62bcede669d486eeb42aa33382800217057612a9bfe2fea64fb179af46a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUri]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a955ee75379fbf48e07d2cbf88001509fa3f47ecc57ae58f10d7539f8362b51(
    *,
    expression: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68501674ddea9d2727ac31e37db602229142920a7bfd0fd941afd80de65f6849(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691d6e8891f0f6af24e1953faaa457e1c76f39d0d1c7a412f12c3b528861cd72(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5544f495fdea8c2b5e1387627444bf107ccc0a19460637d023a9ad54887e25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bdf0983039d81f4a528cbff2e8dd3fc33fcf165520cafe191ad5c06c7bf0a1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713e000cf3d406c05f7f2301475d66cc3df132e9465f98971a877ed4fd787777(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0372b739170083336fde5568727c518fadf195dfc9080ef98eb160bfef458d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriPath]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf010b3a290c16ed74ca1083e4ad536f26c20cb04de60e72ca3b5e2858f7b0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c2710cd7a4a1eb7c9f2da003bd2eab87603f7205d6657a646eab787d8ebf8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1a75c0b9c6445be820eb239229f642f66359b9ed29dab2dd00ec4ceb9f1408(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e72fc8a56ec40a9c549e370e9ae5b83e28859c40d324b78c59d5c1578d2a41e6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriPath]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21c1bf0e13c1ceda03583f316fe8468d17212b7e26e30d5bcf63e16d1757760(
    *,
    expression: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938629a606923dcbfb0c3fb513b70ad39434b129b0b293bec796ae595d6e6ce8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec088b7ecb201465737352b023208328128312748b4b2d5c5f973d9deb57e2aa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69277f448d117284b28c75eb07c22a492c523a8e74b0ad6c83a4bea2b297be3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c8496ed6d092578af403bbb3ddd11cc7bd95ee4ea4893c3835305813748a18(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71722b134c7a25b0a5d7f602bec329bb7dac5c8c515e9c89cf1ee4b1fbed7d43(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a63dc2a82004727eafc326382a430a17dd931896faec6c7842de1b35f314874(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesActionParametersUriQuery]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ede297a8894591be9b9c30bc9f64ebfa264571b2941de78d3c754ba1e5f286(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262195d83903840d6a099c3c7f1821aa294b2460780dd1c4432edb224532068b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16810d5ae7661aeb4c3464ef88e31bd0e8bdde48123ba75fc31aed5bc9c0eaa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7cfe6d676d9f0066a989d6c11b9a5ee9b0121092a73702c052d366cd21da940(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesActionParametersUriQuery]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956002fea91217de0bd013500bd1ef43ec0fa1bc2078234a10de02df91cc0462(
    *,
    password_expression: typing.Optional[builtins.str] = None,
    username_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5595526cc147f2f4b3f23d8e6796b5a33d33718550e7f51daebaab0c9aa59f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c070771cd0bc5fa8a392fe76e34ce6eefd1ce34f76d50d94165b714eaaf5923(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37c88dec41bc1ec0661928ff6f01cf35d8b897c5dea74d3fb5d2e234443818b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80454991f875c602ba0337b7b54ee644027b1402d348113c2f48d5635b1501df(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63e7718c0b277563d697bbe63bc64b2d01e8ada50cadbf6ff1c44fb3a0cc3dfb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2474850e5ed795ca4fe3cec0f56f9874f0baa9bdd41d57d464c1042d94313aea(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesExposedCredentialCheck]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a9b0dc4f1ff94118d2e581e0fb2256d3d6eb7e68b74e709d36deb99cc45e6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bfb41d321fcf5927e6ea78927aaa8b545d2c8760fc5b1753d92c4c27a9ad4bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6232ccb306b8b31dc67c2956febb52c394365472080160fd2d378d8de21437(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a3f117a889d41b6406bd4c8973c3668a67d92be1caa188f5a1a602cb059998(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesExposedCredentialCheck]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b638a57ff40e9d87e75f857c9dcf5112e9cad13a2e6f6a836f152c60ecaf62d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa82498c7685c5e3a26657e17a0b5281530cf63bdf27d82ff84bf9dee51562a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ec520600d8cdb68e796d3434bc7e7d88f1e6c28cd889c617a411994bc89a7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cc599c63fe0e23ac63fd5aefb176ca53d7831d0210d0ed60fd38147effee3b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5529a232890ade1bb6e492549ed37ac4a9a63858de3cba7fa62164bdd8f52686(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94e3fa75e0dc8a2c0a95a56412fdfc5cea96ec8cc784cbbcc636696e9922585(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a615d8f0db2555d02e911e4d5bdb12a8a1e08d20f1dcdae89d5774dfb9adee4b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c102042ab2f01dd08439bd1049c1a8303a836d47c4adf865e2dc514d2e6a38d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d6380cf52e0d0f34fa36e9daba079adc0c79e496f02d711cfa7f4509db44d0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213cbf5bbf47fc09f35add293e18bf22bccf5df4648f0ae94c02630c0f55e2de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d62a9a7a01822d52b278ee0cb251f54a95eb82bb09dd95d41f934bb3e4a00bb1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__410f068d5872b8a21487ccc249a4fe1d8897882b011ff9e587c84ba26182d8a8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d5c8e7196e084f694ca8f11285a626ffb924e49eb5badd67b57b09d4387349(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesLogging]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a6be262230df1f4045ee59501803ffc3c3757d7c51b2db189d29fd1c4ecb69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31729ddd5eb3571f88bd3c3822868e036521763a96005d2b72d85de49c93b62d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338080b0388c6eb6ae350ac113f4dd63ecd19345043e1f0dbab773c641a7d43f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesLogging]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232bfcbec9876f2e54ae7067e9d0e1b09aefe8dcf9eb73e7090575aa463eb9a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f5531cb4544db9cbbdfbfbbc0976e14d0fd92bf735ffdea7b65a5cf554651c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd272e0a472c2853cc489063505d21a4a2c7c92a91fe883d5d1abff1c9cc743(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesExposedCredentialCheck, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1fa5fe2dd18e82255398b45180aa2ff6a4b821e771fab5a3167b7719c06ef4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesLogging, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e335db7da764f664bbf07dc612e19ac7eb5b56b44b8e06983c2188f9b71f6f0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RulesetRulesRatelimit, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a8b2051ba3e07c8fd8efd2be9075b43c5332eb9ea5d51df10a4d77b49d545a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391a57355cb044a3d1a304c34d98e3df61c0f2d220fa879755af9013eca7f917(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4ddc321d90d7d6c8244ca6bb0ce532d0b5bba27d82bec38580fc874d181c2a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b149f46dbbabe23673615237b47b107721f12fd1ac7d54e6b4f3a4eb15dda3e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496453f1fad09ad9a80bb1979431bc1fec98331b67f7871acffbca853e08bcc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8973b6913b6b80c7a2af15ecf906d5cbada26f8cee96a00a537f8267db359fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRules]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9146fcba83927550bd6dd9fbb5fbeaf988f9ce03cbdc34fcc4c0127b518756(
    *,
    characteristics: typing.Optional[typing.Sequence[builtins.str]] = None,
    counting_expression: typing.Optional[builtins.str] = None,
    mitigation_timeout: typing.Optional[jsii.Number] = None,
    period: typing.Optional[jsii.Number] = None,
    requests_per_period: typing.Optional[jsii.Number] = None,
    requests_to_origin: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    score_per_period: typing.Optional[jsii.Number] = None,
    score_response_header_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ed52014a7b40a4311f2ffdac2a7391b549d2e4ef55fad79a67e0d841732981(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a3748e04283904431acf3f1fea20683b207ce02eb7b81f9bbecc35d7826b36(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd04c0ed2f10d167ad2df21735c239b6dc0a3c50da18d3c65b7f63afe14e60e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c77c1786df91710e3c705f3e0512ca3ea0f0c04df3d50d42004b402ecb61ee(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d960f42ec6b1275b6e5fd9318fa586745d98a49b86f867a76942f66b78b35f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71bed2cb577dc3e51ca6484851e2594cfe57f0ce68f21d0d943189cd6ba51554(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RulesetRulesRatelimit]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c616591c8da5a491380cdf450e548e21031b87e9294646f85449ca6876de3b59(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b0cd48e1ff7c508e618a16911b45ce274e1ffa1e9b477882d96de1d6657118(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2562c7127d2dfa33fefd0f6bffde74b783643c9d8d13d33c50f91cfd3c0265(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52721aa2d2a6c39fa5cf18c5be98c7ab022440a4a608d2d192c169ac6ffbbb96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb40c77672534d59de8ef1ca7aa3bec4e1cfe1e8582845e31280adf823c8a5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59eeef774c6a88cd0adcc2d1a084d51cf25eaa2d723e8ccd646573900edbee8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b863854fabfaf4e822152022ad0a713953d1e8f06320a7ec6553135b0ee6f08d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f564e8f18061972b7dd3664a4835038d5fa7ab965351ddebe57ebbed7ae50b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84df3339578e8903f2849e365c7e2772c60aa07c8630705fe9eb977c8b7e05a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57f640f30ff5cf10d412277ad7c65dbd58dd9da5260bea32529a5d8f1192980(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RulesetRulesRatelimit]],
) -> None:
    """Type checking stubs"""
    pass
