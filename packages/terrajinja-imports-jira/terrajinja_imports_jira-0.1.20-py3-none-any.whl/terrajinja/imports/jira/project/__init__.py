'''
# `jira_project`

Refer to the Terraform Registry for docs: [`jira_project`](https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project).
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


class Project(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.project.Project",
):
    '''Represents a {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project jira_project}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        key: builtins.str,
        name: builtins.str,
        assignee_type: typing.Optional[builtins.str] = None,
        avatar_id: typing.Optional[jsii.Number] = None,
        category_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        issue_security_scheme: typing.Optional[jsii.Number] = None,
        lead: typing.Optional[builtins.str] = None,
        lead_account_id: typing.Optional[builtins.str] = None,
        notification_scheme: typing.Optional[jsii.Number] = None,
        permission_scheme: typing.Optional[jsii.Number] = None,
        project_template_key: typing.Optional[builtins.str] = None,
        project_type_key: typing.Optional[builtins.str] = None,
        shared_configuration_project_id: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project jira_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#key Project#key}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#name Project#name}.
        :param assignee_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#assignee_type Project#assignee_type}.
        :param avatar_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#avatar_id Project#avatar_id}.
        :param category_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#category_id Project#category_id}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#description Project#description}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issue_security_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#issue_security_scheme Project#issue_security_scheme}.
        :param lead: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead Project#lead}.
        :param lead_account_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead_account_id Project#lead_account_id}.
        :param notification_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#notification_scheme Project#notification_scheme}.
        :param permission_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#permission_scheme Project#permission_scheme}.
        :param project_template_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_template_key Project#project_template_key}.
        :param project_type_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_type_key Project#project_type_key}.
        :param shared_configuration_project_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#shared_configuration_project_id Project#shared_configuration_project_id}.
        :param url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#url Project#url}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c38c678df856fa75523560de497e4ac4ee2d76dc5d0534bb698cfa712c4f92c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectConfig(
            key=key,
            name=name,
            assignee_type=assignee_type,
            avatar_id=avatar_id,
            category_id=category_id,
            description=description,
            id=id,
            issue_security_scheme=issue_security_scheme,
            lead=lead,
            lead_account_id=lead_account_id,
            notification_scheme=notification_scheme,
            permission_scheme=permission_scheme,
            project_template_key=project_template_key,
            project_type_key=project_type_key,
            shared_configuration_project_id=shared_configuration_project_id,
            url=url,
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
        '''Generates CDKTF code for importing a Project resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Project to import.
        :param import_from_id: The id of the existing Project that should be imported. Refer to the {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Project to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eae5b12f6ce0d729cd33745fe0a70683f872e5eca50288de82067b4014c0972)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAssigneeType")
    def reset_assignee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssigneeType", []))

    @jsii.member(jsii_name="resetAvatarId")
    def reset_avatar_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvatarId", []))

    @jsii.member(jsii_name="resetCategoryId")
    def reset_category_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssueSecurityScheme")
    def reset_issue_security_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssueSecurityScheme", []))

    @jsii.member(jsii_name="resetLead")
    def reset_lead(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLead", []))

    @jsii.member(jsii_name="resetLeadAccountId")
    def reset_lead_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLeadAccountId", []))

    @jsii.member(jsii_name="resetNotificationScheme")
    def reset_notification_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationScheme", []))

    @jsii.member(jsii_name="resetPermissionScheme")
    def reset_permission_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionScheme", []))

    @jsii.member(jsii_name="resetProjectTemplateKey")
    def reset_project_template_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectTemplateKey", []))

    @jsii.member(jsii_name="resetProjectTypeKey")
    def reset_project_type_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectTypeKey", []))

    @jsii.member(jsii_name="resetSharedConfigurationProjectId")
    def reset_shared_configuration_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedConfigurationProjectId", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

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
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="assigneeTypeInput")
    def assignee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assigneeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="avatarIdInput")
    def avatar_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "avatarIdInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryIdInput")
    def category_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issueSecuritySchemeInput")
    def issue_security_scheme_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "issueSecuritySchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="leadAccountIdInput")
    def lead_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "leadAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="leadInput")
    def lead_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "leadInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationSchemeInput")
    def notification_scheme_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "notificationSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionSchemeInput")
    def permission_scheme_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "permissionSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="projectTemplateKeyInput")
    def project_template_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectTemplateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectTypeKeyInput")
    def project_type_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectTypeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedConfigurationProjectIdInput")
    def shared_configuration_project_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sharedConfigurationProjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="assigneeType")
    def assignee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assigneeType"))

    @assignee_type.setter
    def assignee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12003ec1c1ab1c2e318863090e239f106c76304c912bc2c858131a4eed7347c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assigneeType", value)

    @builtins.property
    @jsii.member(jsii_name="avatarId")
    def avatar_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "avatarId"))

    @avatar_id.setter
    def avatar_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef66a6c1f7a6bc2993b1f9ef1179422ac034460464edc63296202a63e3a565bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "avatarId", value)

    @builtins.property
    @jsii.member(jsii_name="categoryId")
    def category_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "categoryId"))

    @category_id.setter
    def category_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8863e40615ac2c57f068c2d9bd01cde9566a81cb0975ae1f7c81b8186dad00a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c42c092974a81e95d560e86cf01fc5f9450693412481e55bb39cc4d127f9578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2ee9b2731e014faf49d1785ea45a141d9aa0b65ca3b2b2c296359a5cdfa432b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issueSecurityScheme")
    def issue_security_scheme(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "issueSecurityScheme"))

    @issue_security_scheme.setter
    def issue_security_scheme(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b18e0f3d935e796779d6df367f03d8f4e5d903b85f508b585c41e6191b6f570)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issueSecurityScheme", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be6b3acc67e4ca32c37ab7afc67b1e2742669ee5794826553efe20d8d4271543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="lead")
    def lead(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lead"))

    @lead.setter
    def lead(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d352b6a3b09737ec917195324f188947a70aa91c43626b85b3a23aa81c86097a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lead", value)

    @builtins.property
    @jsii.member(jsii_name="leadAccountId")
    def lead_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leadAccountId"))

    @lead_account_id.setter
    def lead_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a092e24ffd08b39a2bfdcc773d7290facde3ff62ad029e489f64455d6d450e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "leadAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320708278de3d57210ba33586ed0bb6ecaf258fb69b4c404a1589bddde4c131f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationScheme")
    def notification_scheme(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "notificationScheme"))

    @notification_scheme.setter
    def notification_scheme(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3f0a400bbca7459d4988af590944ba766d67095768efe4190be2a23d494989)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationScheme", value)

    @builtins.property
    @jsii.member(jsii_name="permissionScheme")
    def permission_scheme(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "permissionScheme"))

    @permission_scheme.setter
    def permission_scheme(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e44c530dad307748244ff49e834afd8e96c488aab3f0faa49569301788e57d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionScheme", value)

    @builtins.property
    @jsii.member(jsii_name="projectTemplateKey")
    def project_template_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectTemplateKey"))

    @project_template_key.setter
    def project_template_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03393e61eac64230ce8506f2b388aeeb1655225d8f9bdeb655decbffbc041808)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectTemplateKey", value)

    @builtins.property
    @jsii.member(jsii_name="projectTypeKey")
    def project_type_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectTypeKey"))

    @project_type_key.setter
    def project_type_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d640e6626e3b7ee76073116e99a95255185d82598a3e12f0fc5bb195c841866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectTypeKey", value)

    @builtins.property
    @jsii.member(jsii_name="sharedConfigurationProjectId")
    def shared_configuration_project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sharedConfigurationProjectId"))

    @shared_configuration_project_id.setter
    def shared_configuration_project_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2630bbe9a245d752d1b4bd94b3c26559fe501cb922185bdcdd71b2ca8f608fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedConfigurationProjectId", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9ca444189cb06972588c1a6a3b58b289ddfdc22e569751965f962d3ec94e5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="jira.project.ProjectConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key": "key",
        "name": "name",
        "assignee_type": "assigneeType",
        "avatar_id": "avatarId",
        "category_id": "categoryId",
        "description": "description",
        "id": "id",
        "issue_security_scheme": "issueSecurityScheme",
        "lead": "lead",
        "lead_account_id": "leadAccountId",
        "notification_scheme": "notificationScheme",
        "permission_scheme": "permissionScheme",
        "project_template_key": "projectTemplateKey",
        "project_type_key": "projectTypeKey",
        "shared_configuration_project_id": "sharedConfigurationProjectId",
        "url": "url",
    },
)
class ProjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        key: builtins.str,
        name: builtins.str,
        assignee_type: typing.Optional[builtins.str] = None,
        avatar_id: typing.Optional[jsii.Number] = None,
        category_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        issue_security_scheme: typing.Optional[jsii.Number] = None,
        lead: typing.Optional[builtins.str] = None,
        lead_account_id: typing.Optional[builtins.str] = None,
        notification_scheme: typing.Optional[jsii.Number] = None,
        permission_scheme: typing.Optional[jsii.Number] = None,
        project_template_key: typing.Optional[builtins.str] = None,
        project_type_key: typing.Optional[builtins.str] = None,
        shared_configuration_project_id: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#key Project#key}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#name Project#name}.
        :param assignee_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#assignee_type Project#assignee_type}.
        :param avatar_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#avatar_id Project#avatar_id}.
        :param category_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#category_id Project#category_id}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#description Project#description}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issue_security_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#issue_security_scheme Project#issue_security_scheme}.
        :param lead: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead Project#lead}.
        :param lead_account_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead_account_id Project#lead_account_id}.
        :param notification_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#notification_scheme Project#notification_scheme}.
        :param permission_scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#permission_scheme Project#permission_scheme}.
        :param project_template_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_template_key Project#project_template_key}.
        :param project_type_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_type_key Project#project_type_key}.
        :param shared_configuration_project_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#shared_configuration_project_id Project#shared_configuration_project_id}.
        :param url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#url Project#url}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a0e192c8cda003fb35fad9b2ee5fe336ca63d67ad2d13b22ed83f44a7bfc31)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument assignee_type", value=assignee_type, expected_type=type_hints["assignee_type"])
            check_type(argname="argument avatar_id", value=avatar_id, expected_type=type_hints["avatar_id"])
            check_type(argname="argument category_id", value=category_id, expected_type=type_hints["category_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issue_security_scheme", value=issue_security_scheme, expected_type=type_hints["issue_security_scheme"])
            check_type(argname="argument lead", value=lead, expected_type=type_hints["lead"])
            check_type(argname="argument lead_account_id", value=lead_account_id, expected_type=type_hints["lead_account_id"])
            check_type(argname="argument notification_scheme", value=notification_scheme, expected_type=type_hints["notification_scheme"])
            check_type(argname="argument permission_scheme", value=permission_scheme, expected_type=type_hints["permission_scheme"])
            check_type(argname="argument project_template_key", value=project_template_key, expected_type=type_hints["project_template_key"])
            check_type(argname="argument project_type_key", value=project_type_key, expected_type=type_hints["project_type_key"])
            check_type(argname="argument shared_configuration_project_id", value=shared_configuration_project_id, expected_type=type_hints["shared_configuration_project_id"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
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
        if assignee_type is not None:
            self._values["assignee_type"] = assignee_type
        if avatar_id is not None:
            self._values["avatar_id"] = avatar_id
        if category_id is not None:
            self._values["category_id"] = category_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if issue_security_scheme is not None:
            self._values["issue_security_scheme"] = issue_security_scheme
        if lead is not None:
            self._values["lead"] = lead
        if lead_account_id is not None:
            self._values["lead_account_id"] = lead_account_id
        if notification_scheme is not None:
            self._values["notification_scheme"] = notification_scheme
        if permission_scheme is not None:
            self._values["permission_scheme"] = permission_scheme
        if project_template_key is not None:
            self._values["project_template_key"] = project_template_key
        if project_type_key is not None:
            self._values["project_type_key"] = project_type_key
        if shared_configuration_project_id is not None:
            self._values["shared_configuration_project_id"] = shared_configuration_project_id
        if url is not None:
            self._values["url"] = url

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
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#key Project#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#name Project#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignee_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#assignee_type Project#assignee_type}.'''
        result = self._values.get("assignee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def avatar_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#avatar_id Project#avatar_id}.'''
        result = self._values.get("avatar_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def category_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#category_id Project#category_id}.'''
        result = self._values.get("category_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#description Project#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#id Project#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issue_security_scheme(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#issue_security_scheme Project#issue_security_scheme}.'''
        result = self._values.get("issue_security_scheme")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lead(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead Project#lead}.'''
        result = self._values.get("lead")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lead_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#lead_account_id Project#lead_account_id}.'''
        result = self._values.get("lead_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_scheme(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#notification_scheme Project#notification_scheme}.'''
        result = self._values.get("notification_scheme")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def permission_scheme(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#permission_scheme Project#permission_scheme}.'''
        result = self._values.get("permission_scheme")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project_template_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_template_key Project#project_template_key}.'''
        result = self._values.get("project_template_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_type_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#project_type_key Project#project_type_key}.'''
        result = self._values.get("project_type_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_configuration_project_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#shared_configuration_project_id Project#shared_configuration_project_id}.'''
        result = self._values.get("shared_configuration_project_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/project#url Project#url}.'''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Project",
    "ProjectConfig",
]

publication.publish()

def _typecheckingstub__c38c678df856fa75523560de497e4ac4ee2d76dc5d0534bb698cfa712c4f92c7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    key: builtins.str,
    name: builtins.str,
    assignee_type: typing.Optional[builtins.str] = None,
    avatar_id: typing.Optional[jsii.Number] = None,
    category_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    issue_security_scheme: typing.Optional[jsii.Number] = None,
    lead: typing.Optional[builtins.str] = None,
    lead_account_id: typing.Optional[builtins.str] = None,
    notification_scheme: typing.Optional[jsii.Number] = None,
    permission_scheme: typing.Optional[jsii.Number] = None,
    project_template_key: typing.Optional[builtins.str] = None,
    project_type_key: typing.Optional[builtins.str] = None,
    shared_configuration_project_id: typing.Optional[jsii.Number] = None,
    url: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5eae5b12f6ce0d729cd33745fe0a70683f872e5eca50288de82067b4014c0972(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12003ec1c1ab1c2e318863090e239f106c76304c912bc2c858131a4eed7347c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef66a6c1f7a6bc2993b1f9ef1179422ac034460464edc63296202a63e3a565bd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8863e40615ac2c57f068c2d9bd01cde9566a81cb0975ae1f7c81b8186dad00a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c42c092974a81e95d560e86cf01fc5f9450693412481e55bb39cc4d127f9578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ee9b2731e014faf49d1785ea45a141d9aa0b65ca3b2b2c296359a5cdfa432b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b18e0f3d935e796779d6df367f03d8f4e5d903b85f508b585c41e6191b6f570(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6b3acc67e4ca32c37ab7afc67b1e2742669ee5794826553efe20d8d4271543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d352b6a3b09737ec917195324f188947a70aa91c43626b85b3a23aa81c86097a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a092e24ffd08b39a2bfdcc773d7290facde3ff62ad029e489f64455d6d450e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320708278de3d57210ba33586ed0bb6ecaf258fb69b4c404a1589bddde4c131f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3f0a400bbca7459d4988af590944ba766d67095768efe4190be2a23d494989(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e44c530dad307748244ff49e834afd8e96c488aab3f0faa49569301788e57d0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03393e61eac64230ce8506f2b388aeeb1655225d8f9bdeb655decbffbc041808(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d640e6626e3b7ee76073116e99a95255185d82598a3e12f0fc5bb195c841866(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2630bbe9a245d752d1b4bd94b3c26559fe501cb922185bdcdd71b2ca8f608fe8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9ca444189cb06972588c1a6a3b58b289ddfdc22e569751965f962d3ec94e5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a0e192c8cda003fb35fad9b2ee5fe336ca63d67ad2d13b22ed83f44a7bfc31(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    key: builtins.str,
    name: builtins.str,
    assignee_type: typing.Optional[builtins.str] = None,
    avatar_id: typing.Optional[jsii.Number] = None,
    category_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    issue_security_scheme: typing.Optional[jsii.Number] = None,
    lead: typing.Optional[builtins.str] = None,
    lead_account_id: typing.Optional[builtins.str] = None,
    notification_scheme: typing.Optional[jsii.Number] = None,
    permission_scheme: typing.Optional[jsii.Number] = None,
    project_template_key: typing.Optional[builtins.str] = None,
    project_type_key: typing.Optional[builtins.str] = None,
    shared_configuration_project_id: typing.Optional[jsii.Number] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
