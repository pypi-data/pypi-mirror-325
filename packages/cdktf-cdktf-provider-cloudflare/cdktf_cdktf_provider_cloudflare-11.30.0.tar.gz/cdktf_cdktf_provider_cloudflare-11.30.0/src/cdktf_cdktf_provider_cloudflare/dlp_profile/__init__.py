r'''
# `cloudflare_dlp_profile`

Refer to the Terraform Registry for docs: [`cloudflare_dlp_profile`](https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile).
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


class DlpProfile(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfile",
):
    '''Represents a {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile cloudflare_dlp_profile}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        allowed_match_count: jsii.Number,
        entry: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlpProfileEntry", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        type: builtins.str,
        context_awareness: typing.Optional[typing.Union["DlpProfileContextAwareness", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ocr_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile cloudflare_dlp_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#account_id DlpProfile#account_id}
        :param allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#allowed_match_count DlpProfile#allowed_match_count}
        :param entry: entry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#entry DlpProfile#entry}
        :param name: Name of the profile. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#name DlpProfile#name}
        :param type: The type of the profile. Available values: ``custom``, ``predefined``. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#type DlpProfile#type}
        :param context_awareness: context_awareness block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#context_awareness DlpProfile#context_awareness}
        :param description: Brief summary of the profile and its intended use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#description DlpProfile#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#id DlpProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ocr_enabled: If true, scan images via OCR to determine if any text present matches filters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#ocr_enabled DlpProfile#ocr_enabled}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f111ba0edf2064331c52e0b522b7fd87e658d1e0dacd2175df17d18507e592f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DlpProfileConfig(
            account_id=account_id,
            allowed_match_count=allowed_match_count,
            entry=entry,
            name=name,
            type=type,
            context_awareness=context_awareness,
            description=description,
            id=id,
            ocr_enabled=ocr_enabled,
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
        '''Generates CDKTF code for importing a DlpProfile resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DlpProfile to import.
        :param import_from_id: The id of the existing DlpProfile that should be imported. Refer to the {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DlpProfile to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a33d670364b7ae861bcb63316797da062b9584a568e0948289b37520046350)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putContextAwareness")
    def put_context_awareness(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        skip: typing.Union["DlpProfileContextAwarenessSkip", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param enabled: Scan the context of predefined entries to only return matches surrounded by keywords. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#enabled DlpProfile#enabled}
        :param skip: skip block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#skip DlpProfile#skip}
        '''
        value = DlpProfileContextAwareness(enabled=enabled, skip=skip)

        return typing.cast(None, jsii.invoke(self, "putContextAwareness", [value]))

    @jsii.member(jsii_name="putEntry")
    def put_entry(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlpProfileEntry", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1780f01df8e68426aec9a45a7d24e1c620e7ccbc51bfbce6a288493da573ced2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntry", [value]))

    @jsii.member(jsii_name="resetContextAwareness")
    def reset_context_awareness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextAwareness", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOcrEnabled")
    def reset_ocr_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcrEnabled", []))

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
    @jsii.member(jsii_name="contextAwareness")
    def context_awareness(self) -> "DlpProfileContextAwarenessOutputReference":
        return typing.cast("DlpProfileContextAwarenessOutputReference", jsii.get(self, "contextAwareness"))

    @builtins.property
    @jsii.member(jsii_name="entry")
    def entry(self) -> "DlpProfileEntryList":
        return typing.cast("DlpProfileEntryList", jsii.get(self, "entry"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMatchCountInput")
    def allowed_match_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allowedMatchCountInput"))

    @builtins.property
    @jsii.member(jsii_name="contextAwarenessInput")
    def context_awareness_input(self) -> typing.Optional["DlpProfileContextAwareness"]:
        return typing.cast(typing.Optional["DlpProfileContextAwareness"], jsii.get(self, "contextAwarenessInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="entryInput")
    def entry_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlpProfileEntry"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlpProfileEntry"]]], jsii.get(self, "entryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ocrEnabledInput")
    def ocr_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ocrEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c34dffe81918afb5fb633c22f0523f1abb24628e87dfae69e66207d21a516f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowedMatchCount")
    def allowed_match_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allowedMatchCount"))

    @allowed_match_count.setter
    def allowed_match_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bcdf54b56703bf9bf0d8421021ca504ce479a0d80574f3c7c0310cb4db985e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMatchCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64de3267213e8a9f8a5192aa52b18fe5e797494e130c244028c483a194410c36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865b327c9af4350b254084cf52fa31a19ad1adf7afbda8627339e7651c203bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4485eb72d7c46481658c673444358d83a7b77bba120ddd017f5d5c61bd06acdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ocrEnabled")
    def ocr_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ocrEnabled"))

    @ocr_enabled.setter
    def ocr_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74a5e315c91867c13354f2a08a96a911f18b47e056a4a2a16e16dd613055c603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocrEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e8c5f71dc41977523bbe3712ce3fe6af06f7baf31dbdc8ea51b1689863a902f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "allowed_match_count": "allowedMatchCount",
        "entry": "entry",
        "name": "name",
        "type": "type",
        "context_awareness": "contextAwareness",
        "description": "description",
        "id": "id",
        "ocr_enabled": "ocrEnabled",
    },
)
class DlpProfileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_id: builtins.str,
        allowed_match_count: jsii.Number,
        entry: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlpProfileEntry", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        type: builtins.str,
        context_awareness: typing.Optional[typing.Union["DlpProfileContextAwareness", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ocr_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#account_id DlpProfile#account_id}
        :param allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#allowed_match_count DlpProfile#allowed_match_count}
        :param entry: entry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#entry DlpProfile#entry}
        :param name: Name of the profile. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#name DlpProfile#name}
        :param type: The type of the profile. Available values: ``custom``, ``predefined``. **Modifying this attribute will force creation of a new resource.**. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#type DlpProfile#type}
        :param context_awareness: context_awareness block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#context_awareness DlpProfile#context_awareness}
        :param description: Brief summary of the profile and its intended use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#description DlpProfile#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#id DlpProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ocr_enabled: If true, scan images via OCR to determine if any text present matches filters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#ocr_enabled DlpProfile#ocr_enabled}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(context_awareness, dict):
            context_awareness = DlpProfileContextAwareness(**context_awareness)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5686f9d040f555a6523124f06b4df1cc6e96f35bbc56d65bf132cdb61097e22c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument allowed_match_count", value=allowed_match_count, expected_type=type_hints["allowed_match_count"])
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument context_awareness", value=context_awareness, expected_type=type_hints["context_awareness"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ocr_enabled", value=ocr_enabled, expected_type=type_hints["ocr_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "allowed_match_count": allowed_match_count,
            "entry": entry,
            "name": name,
            "type": type,
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
        if context_awareness is not None:
            self._values["context_awareness"] = context_awareness
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if ocr_enabled is not None:
            self._values["ocr_enabled"] = ocr_enabled

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
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#account_id DlpProfile#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_match_count(self) -> jsii.Number:
        '''Related DLP policies will trigger when the match count exceeds the number set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#allowed_match_count DlpProfile#allowed_match_count}
        '''
        result = self._values.get("allowed_match_count")
        assert result is not None, "Required property 'allowed_match_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def entry(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlpProfileEntry"]]:
        '''entry block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#entry DlpProfile#entry}
        '''
        result = self._values.get("entry")
        assert result is not None, "Required property 'entry' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlpProfileEntry"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the profile. **Modifying this attribute will force creation of a new resource.**.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#name DlpProfile#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the profile. Available values: ``custom``, ``predefined``. **Modifying this attribute will force creation of a new resource.**.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#type DlpProfile#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context_awareness(self) -> typing.Optional["DlpProfileContextAwareness"]:
        '''context_awareness block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#context_awareness DlpProfile#context_awareness}
        '''
        result = self._values.get("context_awareness")
        return typing.cast(typing.Optional["DlpProfileContextAwareness"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Brief summary of the profile and its intended use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#description DlpProfile#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#id DlpProfile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ocr_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, scan images via OCR to determine if any text present matches filters.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#ocr_enabled DlpProfile#ocr_enabled}
        '''
        result = self._values.get("ocr_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlpProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileContextAwareness",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "skip": "skip"},
)
class DlpProfileContextAwareness:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        skip: typing.Union["DlpProfileContextAwarenessSkip", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param enabled: Scan the context of predefined entries to only return matches surrounded by keywords. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#enabled DlpProfile#enabled}
        :param skip: skip block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#skip DlpProfile#skip}
        '''
        if isinstance(skip, dict):
            skip = DlpProfileContextAwarenessSkip(**skip)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e915da2f82928f038a021de53f5afcb1464ec379f845b2cd54dbede7be7e979)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument skip", value=skip, expected_type=type_hints["skip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
            "skip": skip,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Scan the context of predefined entries to only return matches surrounded by keywords.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#enabled DlpProfile#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def skip(self) -> "DlpProfileContextAwarenessSkip":
        '''skip block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#skip DlpProfile#skip}
        '''
        result = self._values.get("skip")
        assert result is not None, "Required property 'skip' is missing"
        return typing.cast("DlpProfileContextAwarenessSkip", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlpProfileContextAwareness(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlpProfileContextAwarenessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileContextAwarenessOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b992c16d9bbe617d94450f684071932ae891df42d3bb249a098975b418fb7859)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSkip")
    def put_skip(
        self,
        *,
        files: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param files: Return all matches, regardless of context analysis result, if the data is a file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#files DlpProfile#files}
        '''
        value = DlpProfileContextAwarenessSkip(files=files)

        return typing.cast(None, jsii.invoke(self, "putSkip", [value]))

    @builtins.property
    @jsii.member(jsii_name="skip")
    def skip(self) -> "DlpProfileContextAwarenessSkipOutputReference":
        return typing.cast("DlpProfileContextAwarenessSkipOutputReference", jsii.get(self, "skip"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="skipInput")
    def skip_input(self) -> typing.Optional["DlpProfileContextAwarenessSkip"]:
        return typing.cast(typing.Optional["DlpProfileContextAwarenessSkip"], jsii.get(self, "skipInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__346c2951c80ad3f2d668eb6db5db8259623a7fab7146a1987aaf6f74eecfa579)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DlpProfileContextAwareness]:
        return typing.cast(typing.Optional[DlpProfileContextAwareness], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlpProfileContextAwareness],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cfdbf7f48d7ac72b2236482a8e035ae0a5375e2213c2573da20bf49046ec80a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileContextAwarenessSkip",
    jsii_struct_bases=[],
    name_mapping={"files": "files"},
)
class DlpProfileContextAwarenessSkip:
    def __init__(
        self,
        *,
        files: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param files: Return all matches, regardless of context analysis result, if the data is a file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#files DlpProfile#files}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e92711d1fd33cfca997a0a874ca9e6bf27e54ad3af05c7a6ed0b0d0448fb2d)
            check_type(argname="argument files", value=files, expected_type=type_hints["files"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "files": files,
        }

    @builtins.property
    def files(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Return all matches, regardless of context analysis result, if the data is a file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#files DlpProfile#files}
        '''
        result = self._values.get("files")
        assert result is not None, "Required property 'files' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlpProfileContextAwarenessSkip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlpProfileContextAwarenessSkipOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileContextAwarenessSkipOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986d2166ff4f598be948eca9ab9eb04bae9a23c820d8aaeac2eaedea4404feee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="filesInput")
    def files_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "filesInput"))

    @builtins.property
    @jsii.member(jsii_name="files")
    def files(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "files"))

    @files.setter
    def files(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbfc02f1f32c44f272dd3af88688877ffc9432d6cb24d621d3b704655c0b371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "files", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DlpProfileContextAwarenessSkip]:
        return typing.cast(typing.Optional[DlpProfileContextAwarenessSkip], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlpProfileContextAwarenessSkip],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fade665de5904e7aabca153cc62d3ca99bb6d814e9b6498ae93ed4edf1702f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileEntry",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "enabled": "enabled",
        "id": "id",
        "pattern": "pattern",
    },
)
class DlpProfileEntry:
    def __init__(
        self,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[typing.Union["DlpProfileEntryPattern", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the entry to deploy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#name DlpProfile#name}
        :param enabled: Whether the entry is active. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#enabled DlpProfile#enabled}
        :param id: Unique entry identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#id DlpProfile#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pattern: pattern block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#pattern DlpProfile#pattern}
        '''
        if isinstance(pattern, dict):
            pattern = DlpProfileEntryPattern(**pattern)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d1e56e4d31bca24fcddf5ef6f02327f765db0793b54629b11341d973c9d7965)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if pattern is not None:
            self._values["pattern"] = pattern

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the entry to deploy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#name DlpProfile#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the entry is active. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#enabled DlpProfile#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique entry identifier.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#id DlpProfile#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional["DlpProfileEntryPattern"]:
        '''pattern block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#pattern DlpProfile#pattern}
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional["DlpProfileEntryPattern"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlpProfileEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlpProfileEntryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileEntryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a682988018e0c22c1cc78f17b86ded4df7806fbd429fba8b74e4abc38397128f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DlpProfileEntryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5d3adb0000329a32a28342c64597adb9a96de48962fd850508ceb8a3472fce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DlpProfileEntryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bc5bea36b5ffa211358a47a90739c92ce4465fe501c65691a10b0c92dc3a0f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c9084bb5b51e163f67ca733172671ba93acac72abed60656fbd0aec22396f6f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4301e84c9993ffbaf0175f6797b63ab976ac62c093cb39d8bcba6a2b9b0852d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlpProfileEntry]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlpProfileEntry]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlpProfileEntry]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb59113620d83fc6717390b95b90fa7cff75ec3b6c2ed1b978599e140c5c926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class DlpProfileEntryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileEntryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__54c8adfd9ca9ddcb651d1ea3f97f322db8f99c105e57a90999dfdf3bc63a4eac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPattern")
    def put_pattern(
        self,
        *,
        regex: builtins.str,
        validation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex: The regex that defines the pattern. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#regex DlpProfile#regex}
        :param validation: The validation algorithm to apply with this pattern. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#validation DlpProfile#validation}
        '''
        value = DlpProfileEntryPattern(regex=regex, validation=validation)

        return typing.cast(None, jsii.invoke(self, "putPattern", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPattern")
    def reset_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPattern", []))

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> "DlpProfileEntryPatternOutputReference":
        return typing.cast("DlpProfileEntryPatternOutputReference", jsii.get(self, "pattern"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional["DlpProfileEntryPattern"]:
        return typing.cast(typing.Optional["DlpProfileEntryPattern"], jsii.get(self, "patternInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__81db675ea97733cdb5401808ffed40d19142fc106ac5dcdacf5c14a03af0ac6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d74b8f8c0b50600d4152fc58af34b08931be2a55168ebae5b8222a9a8a348e8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b14a81a568aa9ff74fea2d666cb65b8663d9066d2fd78661101ea00ce403ffc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DlpProfileEntry]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DlpProfileEntry]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DlpProfileEntry]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03679aa593f60e509501b9d6e1e02d2be2ca0649305d6b3287e3c84e682da3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileEntryPattern",
    jsii_struct_bases=[],
    name_mapping={"regex": "regex", "validation": "validation"},
)
class DlpProfileEntryPattern:
    def __init__(
        self,
        *,
        regex: builtins.str,
        validation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex: The regex that defines the pattern. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#regex DlpProfile#regex}
        :param validation: The validation algorithm to apply with this pattern. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#validation DlpProfile#validation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026c99806fc26cccb41afcb327d74988f78ee9332fabf9f3c483511867eb62a6)
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "regex": regex,
        }
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def regex(self) -> builtins.str:
        '''The regex that defines the pattern.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#regex DlpProfile#regex}
        '''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validation(self) -> typing.Optional[builtins.str]:
        '''The validation algorithm to apply with this pattern.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/dlp_profile#validation DlpProfile#validation}
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlpProfileEntryPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlpProfileEntryPatternOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.dlpProfile.DlpProfileEntryPatternOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__560e254c81c2e068ba85fa3defce6aca165b56e6272b14c7f29fd107a1772b63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetValidation")
    def reset_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidation", []))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09353706e8483d758912333953cfae672c5103affda84b29dc374664fc9f50c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validation"))

    @validation.setter
    def validation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d7e55572218b8300287a5629a8c1b13640738b36cce81cc19809ab34c266d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DlpProfileEntryPattern]:
        return typing.cast(typing.Optional[DlpProfileEntryPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DlpProfileEntryPattern]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dacc8cb9f0b9ec96251704d0c9a165600b23a81a2921e6a9039617916e4a42ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "DlpProfile",
    "DlpProfileConfig",
    "DlpProfileContextAwareness",
    "DlpProfileContextAwarenessOutputReference",
    "DlpProfileContextAwarenessSkip",
    "DlpProfileContextAwarenessSkipOutputReference",
    "DlpProfileEntry",
    "DlpProfileEntryList",
    "DlpProfileEntryOutputReference",
    "DlpProfileEntryPattern",
    "DlpProfileEntryPatternOutputReference",
]

publication.publish()

def _typecheckingstub__f111ba0edf2064331c52e0b522b7fd87e658d1e0dacd2175df17d18507e592f6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_id: builtins.str,
    allowed_match_count: jsii.Number,
    entry: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlpProfileEntry, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    type: builtins.str,
    context_awareness: typing.Optional[typing.Union[DlpProfileContextAwareness, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ocr_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__72a33d670364b7ae861bcb63316797da062b9584a568e0948289b37520046350(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1780f01df8e68426aec9a45a7d24e1c620e7ccbc51bfbce6a288493da573ced2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlpProfileEntry, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c34dffe81918afb5fb633c22f0523f1abb24628e87dfae69e66207d21a516f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcdf54b56703bf9bf0d8421021ca504ce479a0d80574f3c7c0310cb4db985e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64de3267213e8a9f8a5192aa52b18fe5e797494e130c244028c483a194410c36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865b327c9af4350b254084cf52fa31a19ad1adf7afbda8627339e7651c203bf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4485eb72d7c46481658c673444358d83a7b77bba120ddd017f5d5c61bd06acdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a5e315c91867c13354f2a08a96a911f18b47e056a4a2a16e16dd613055c603(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8c5f71dc41977523bbe3712ce3fe6af06f7baf31dbdc8ea51b1689863a902f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5686f9d040f555a6523124f06b4df1cc6e96f35bbc56d65bf132cdb61097e22c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_id: builtins.str,
    allowed_match_count: jsii.Number,
    entry: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlpProfileEntry, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    type: builtins.str,
    context_awareness: typing.Optional[typing.Union[DlpProfileContextAwareness, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ocr_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e915da2f82928f038a021de53f5afcb1464ec379f845b2cd54dbede7be7e979(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    skip: typing.Union[DlpProfileContextAwarenessSkip, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b992c16d9bbe617d94450f684071932ae891df42d3bb249a098975b418fb7859(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346c2951c80ad3f2d668eb6db5db8259623a7fab7146a1987aaf6f74eecfa579(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cfdbf7f48d7ac72b2236482a8e035ae0a5375e2213c2573da20bf49046ec80a(
    value: typing.Optional[DlpProfileContextAwareness],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e92711d1fd33cfca997a0a874ca9e6bf27e54ad3af05c7a6ed0b0d0448fb2d(
    *,
    files: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986d2166ff4f598be948eca9ab9eb04bae9a23c820d8aaeac2eaedea4404feee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbfc02f1f32c44f272dd3af88688877ffc9432d6cb24d621d3b704655c0b371(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fade665de5904e7aabca153cc62d3ca99bb6d814e9b6498ae93ed4edf1702f8(
    value: typing.Optional[DlpProfileContextAwarenessSkip],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d1e56e4d31bca24fcddf5ef6f02327f765db0793b54629b11341d973c9d7965(
    *,
    name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    pattern: typing.Optional[typing.Union[DlpProfileEntryPattern, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a682988018e0c22c1cc78f17b86ded4df7806fbd429fba8b74e4abc38397128f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5d3adb0000329a32a28342c64597adb9a96de48962fd850508ceb8a3472fce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc5bea36b5ffa211358a47a90739c92ce4465fe501c65691a10b0c92dc3a0f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9084bb5b51e163f67ca733172671ba93acac72abed60656fbd0aec22396f6f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4301e84c9993ffbaf0175f6797b63ab976ac62c093cb39d8bcba6a2b9b0852d4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb59113620d83fc6717390b95b90fa7cff75ec3b6c2ed1b978599e140c5c926(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlpProfileEntry]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c8adfd9ca9ddcb651d1ea3f97f322db8f99c105e57a90999dfdf3bc63a4eac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81db675ea97733cdb5401808ffed40d19142fc106ac5dcdacf5c14a03af0ac6a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d74b8f8c0b50600d4152fc58af34b08931be2a55168ebae5b8222a9a8a348e8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b14a81a568aa9ff74fea2d666cb65b8663d9066d2fd78661101ea00ce403ffc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03679aa593f60e509501b9d6e1e02d2be2ca0649305d6b3287e3c84e682da3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DlpProfileEntry]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026c99806fc26cccb41afcb327d74988f78ee9332fabf9f3c483511867eb62a6(
    *,
    regex: builtins.str,
    validation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__560e254c81c2e068ba85fa3defce6aca165b56e6272b14c7f29fd107a1772b63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09353706e8483d758912333953cfae672c5103affda84b29dc374664fc9f50c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d7e55572218b8300287a5629a8c1b13640738b36cce81cc19809ab34c266d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dacc8cb9f0b9ec96251704d0c9a165600b23a81a2921e6a9039617916e4a42ce(
    value: typing.Optional[DlpProfileEntryPattern],
) -> None:
    """Type checking stubs"""
    pass
