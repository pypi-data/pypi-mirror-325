'''
# `jira_filter`

Refer to the Terraform Registry for docs: [`jira_filter`](https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Filter(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.filter.Filter",
):
    '''Represents a {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter jira_filter}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        jql: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        favourite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FilterPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter jira_filter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param jql: JQL expression of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#jql Filter#jql}
        :param name: Name of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#name Filter#name}
        :param description: Description of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#description Filter#description}
        :param favourite: Whether the filter is marked as favorite. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#favourite Filter#favourite}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#id Filter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#permissions Filter#permissions}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7102d20dcf78c6f9a7cfff2dfac5c116eb889933d54a25638403457a70599d64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FilterConfig(
            jql=jql,
            name=name,
            description=description,
            favourite=favourite,
            id=id,
            permissions=permissions,
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
        '''Generates CDKTF code for importing a Filter resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Filter to import.
        :param import_from_id: The id of the existing Filter that should be imported. Refer to the {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Filter to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e4e73c38f9828447b0d4c66de05e98b3b94782dd46a1d93213f2bd3b4eb11a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FilterPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d151f562bd0dff1f23c205d7bd54ea24ddf64e44da39ab7460e3080f49de7210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFavourite")
    def reset_favourite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFavourite", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

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
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "FilterPermissionsList":
        return typing.cast("FilterPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="favouriteInput")
    def favourite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "favouriteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jqlInput")
    def jql_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jqlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FilterPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FilterPermissions"]]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f1c4db0383ff9cfe9618d9b426fe30e1e7c08b5f7516a3ec596ee932eaaf92b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="favourite")
    def favourite(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "favourite"))

    @favourite.setter
    def favourite(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e43203472ad89289fb0727648d98d518d0b2622dc70b31068f587b55ceba621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "favourite", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e90ac8a28a480010729e47f73c22a11e1c8ea5ed6154c7c3e9496ae8cac9455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jql")
    def jql(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jql"))

    @jql.setter
    def jql(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c49ef6f1ca3f8934979aa999e55050d517f6aa21f37830d6b94ac73235d23469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jql", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba4f7ed7f0d7f613f5760f74b63087f0edfd4f5850acbbefeddbb2fda4a21dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="jira.filter.FilterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "jql": "jql",
        "name": "name",
        "description": "description",
        "favourite": "favourite",
        "id": "id",
        "permissions": "permissions",
    },
)
class FilterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        jql: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        favourite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FilterPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param jql: JQL expression of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#jql Filter#jql}
        :param name: Name of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#name Filter#name}
        :param description: Description of the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#description Filter#description}
        :param favourite: Whether the filter is marked as favorite. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#favourite Filter#favourite}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#id Filter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#permissions Filter#permissions}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b097b35d5a27a52e04f0dc6a56ecd009c8656aeda4cceafe0d90dd8eeeb6f1d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument jql", value=jql, expected_type=type_hints["jql"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument favourite", value=favourite, expected_type=type_hints["favourite"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "jql": jql,
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
        if description is not None:
            self._values["description"] = description
        if favourite is not None:
            self._values["favourite"] = favourite
        if id is not None:
            self._values["id"] = id
        if permissions is not None:
            self._values["permissions"] = permissions

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
    def jql(self) -> builtins.str:
        '''JQL expression of the filter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#jql Filter#jql}
        '''
        result = self._values.get("jql")
        assert result is not None, "Required property 'jql' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the filter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#name Filter#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the filter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#description Filter#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def favourite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the filter is marked as favorite.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#favourite Filter#favourite}
        '''
        result = self._values.get("favourite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#id Filter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FilterPermissions"]]]:
        '''permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#permissions Filter#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FilterPermissions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jira.filter.FilterPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "group_name": "groupName",
        "project_id": "projectId",
        "project_role_id": "projectRoleId",
    },
)
class FilterPermissions:
    def __init__(
        self,
        *,
        type: builtins.str,
        group_name: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        project_role_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of the permission. Needs to be one of global, group, project, project_role or authenticated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#type Filter#type}
        :param group_name: All Members of the of this group can access the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#group_name Filter#group_name}
        :param project_id: All Members of the project with the given ID can access the filter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#project_id Filter#project_id}
        :param project_role_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#project_role_id Filter#project_role_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2704ae407996ff6f18d34f8e64084f61c2643bfc5d83a2692cbef37438f3e794)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument project_role_id", value=project_role_id, expected_type=type_hints["project_role_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if group_name is not None:
            self._values["group_name"] = group_name
        if project_id is not None:
            self._values["project_id"] = project_id
        if project_role_id is not None:
            self._values["project_role_id"] = project_role_id

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the permission. Needs to be one of global, group, project, project_role or authenticated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#type Filter#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''All Members of the of this group can access the filter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#group_name Filter#group_name}
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''All Members of the project with the given ID can access the filter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#project_id Filter#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_role_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/filter#project_role_id Filter#project_role_id}.'''
        result = self._values.get("project_role_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FilterPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.filter.FilterPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d95a407118fdda43b1bfdf8d84502226027e128eae2fb261d561783978c43c1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FilterPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b6a5452ef14abb4c00ea9c12737d90d5aac800b11c8c4f6f233a5a531b03e2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FilterPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64082d7cbdc32f578e87fec0f02c629ed1c2a97affa2f213d5e9fb4025e8b0b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b5d7e1a8b16ad07530260e51eae723b8b0e84b1d76f195be879c9754d94dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f14382e5ebf9ee262f2259e7b3bd6cfa1679057697d8573c43d1dae28968c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FilterPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FilterPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FilterPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8e2d99f8c02ae1f95a976abc216a102e21b75a150c43c1b1eb61b5c7b61ad0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FilterPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.filter.FilterPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd13da1fb1096ac32f89917928cc576e367ce252b7e7cd18511962e8f8ead40e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetProjectRoleId")
    def reset_project_role_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectRoleId", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectRoleIdInput")
    def project_role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectRoleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9cbace233d8818aefbf9da8979307a922f8df2b76c2dc379e2c16a47eca331f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af2a71d64825270e4630d8ea1a5ca20e1a69c8d7f978da19cbb74bff41511c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="projectRoleId")
    def project_role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectRoleId"))

    @project_role_id.setter
    def project_role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d84640cab4211380b145203a4bcf5ea893e32df70a11b728e0b8e425d79babe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectRoleId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09b3ff6bc04ca3e928af8f49a899452813cff1aa5e1ce30c7f95f58cdf09f6b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FilterPermissions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FilterPermissions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FilterPermissions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576d22b08a2b532ef42c64db7e0227225937bbe4dd95b188184704fe6e4994c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Filter",
    "FilterConfig",
    "FilterPermissions",
    "FilterPermissionsList",
    "FilterPermissionsOutputReference",
]

publication.publish()

def _typecheckingstub__7102d20dcf78c6f9a7cfff2dfac5c116eb889933d54a25638403457a70599d64(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    jql: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    favourite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FilterPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__46e4e73c38f9828447b0d4c66de05e98b3b94782dd46a1d93213f2bd3b4eb11a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d151f562bd0dff1f23c205d7bd54ea24ddf64e44da39ab7460e3080f49de7210(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FilterPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f1c4db0383ff9cfe9618d9b426fe30e1e7c08b5f7516a3ec596ee932eaaf92b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e43203472ad89289fb0727648d98d518d0b2622dc70b31068f587b55ceba621(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e90ac8a28a480010729e47f73c22a11e1c8ea5ed6154c7c3e9496ae8cac9455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c49ef6f1ca3f8934979aa999e55050d517f6aa21f37830d6b94ac73235d23469(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba4f7ed7f0d7f613f5760f74b63087f0edfd4f5850acbbefeddbb2fda4a21dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b097b35d5a27a52e04f0dc6a56ecd009c8656aeda4cceafe0d90dd8eeeb6f1d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    jql: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    favourite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FilterPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2704ae407996ff6f18d34f8e64084f61c2643bfc5d83a2692cbef37438f3e794(
    *,
    type: builtins.str,
    group_name: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    project_role_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95a407118fdda43b1bfdf8d84502226027e128eae2fb261d561783978c43c1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b6a5452ef14abb4c00ea9c12737d90d5aac800b11c8c4f6f233a5a531b03e2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64082d7cbdc32f578e87fec0f02c629ed1c2a97affa2f213d5e9fb4025e8b0b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b5d7e1a8b16ad07530260e51eae723b8b0e84b1d76f195be879c9754d94dcb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f14382e5ebf9ee262f2259e7b3bd6cfa1679057697d8573c43d1dae28968c6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8e2d99f8c02ae1f95a976abc216a102e21b75a150c43c1b1eb61b5c7b61ad0f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FilterPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd13da1fb1096ac32f89917928cc576e367ce252b7e7cd18511962e8f8ead40e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9cbace233d8818aefbf9da8979307a922f8df2b76c2dc379e2c16a47eca331f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af2a71d64825270e4630d8ea1a5ca20e1a69c8d7f978da19cbb74bff41511c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d84640cab4211380b145203a4bcf5ea893e32df70a11b728e0b8e425d79babe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09b3ff6bc04ca3e928af8f49a899452813cff1aa5e1ce30c7f95f58cdf09f6b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576d22b08a2b532ef42c64db7e0227225937bbe4dd95b188184704fe6e4994c9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FilterPermissions]],
) -> None:
    """Type checking stubs"""
    pass
