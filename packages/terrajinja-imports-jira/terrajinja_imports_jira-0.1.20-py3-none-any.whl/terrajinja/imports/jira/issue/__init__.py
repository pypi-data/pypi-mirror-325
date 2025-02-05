'''
# `jira_issue`

Refer to the Terraform Registry for docs: [`jira_issue`](https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue).
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


class Issue(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.issue.Issue",
):
    '''Represents a {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue jira_issue}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        issue_type: builtins.str,
        project_key: builtins.str,
        summary: builtins.str,
        assignee: typing.Optional[builtins.str] = None,
        delete_transition: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        reporter: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        state_transition: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue jira_issue} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param issue_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#issue_type Issue#issue_type}.
        :param project_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#project_key Issue#project_key}.
        :param summary: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#summary Issue#summary}.
        :param assignee: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#assignee Issue#assignee}.
        :param delete_transition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#delete_transition Issue#delete_transition}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#description Issue#description}.
        :param fields: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#fields Issue#fields}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#id Issue#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#labels Issue#labels}.
        :param reporter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#reporter Issue#reporter}.
        :param state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state Issue#state}.
        :param state_transition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state_transition Issue#state_transition}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef262c703edce4195e5912484af2c857cd26e1c45534dad7eb21e5e47c26e21)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IssueConfig(
            issue_type=issue_type,
            project_key=project_key,
            summary=summary,
            assignee=assignee,
            delete_transition=delete_transition,
            description=description,
            fields=fields,
            id=id,
            labels=labels,
            reporter=reporter,
            state=state,
            state_transition=state_transition,
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
        '''Generates CDKTF code for importing a Issue resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Issue to import.
        :param import_from_id: The id of the existing Issue that should be imported. Refer to the {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Issue to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e9240e44b2c282573a4737a820163ad8423d27d47a08657d3e0c98bcaa4e49)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAssignee")
    def reset_assignee(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignee", []))

    @jsii.member(jsii_name="resetDeleteTransition")
    def reset_delete_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteTransition", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFields")
    def reset_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFields", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetReporter")
    def reset_reporter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReporter", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStateTransition")
    def reset_state_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateTransition", []))

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
    @jsii.member(jsii_name="issueKey")
    def issue_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issueKey"))

    @builtins.property
    @jsii.member(jsii_name="assigneeInput")
    def assignee_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assigneeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteTransitionInput")
    def delete_transition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issueTypeInput")
    def issue_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectKeyInput")
    def project_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="reporterInput")
    def reporter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reporterInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="stateTransitionInput")
    def state_transition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="assignee")
    def assignee(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assignee"))

    @assignee.setter
    def assignee(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dbedaecf2c091e3dd00381bc632d8a19cd74a7098485daaec5edebf79ab6781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignee", value)

    @builtins.property
    @jsii.member(jsii_name="deleteTransition")
    def delete_transition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteTransition"))

    @delete_transition.setter
    def delete_transition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a8663c0e9db70faf7e69770602f8fa7de2eab6b7f1e87045f03efeed647802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteTransition", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfbb41b07a439e3bde9fa0ac3fde2071c2910449ceaf29afba7fb34f905b7c9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "fields"))

    @fields.setter
    def fields(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65f9028ed6be7459f608bc2a17494a29f1c03b36c66f898ca3c64b3b1df351c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b4526e137d050737b4397d092afbd257a89ed2174cac4184db97ed8c3b0e54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issueType")
    def issue_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issueType"))

    @issue_type.setter
    def issue_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b190f246aa6579fdaec04020d883c4512eec9b3881a9bdd45a03b7a5fa07de8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issueType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e331e3a2057a51546cba93c682553189d5838a63ddd3824438a068e7a30a9700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="projectKey")
    def project_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectKey"))

    @project_key.setter
    def project_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ca0003d0e1dbba84af0a8acc84202c9f08271726abd939ccc5a5a787d3410c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectKey", value)

    @builtins.property
    @jsii.member(jsii_name="reporter")
    def reporter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reporter"))

    @reporter.setter
    def reporter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536e4f2e01cecdb23b22747da63abe49b499840e44863f3fc56033995d6ef53c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reporter", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c553e0a18b818d5bb7e4cc1eeb0004293b270247a4632449b30f8c79a30ecd09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="stateTransition")
    def state_transition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateTransition"))

    @state_transition.setter
    def state_transition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2931ccff34eaacb52c1dd7a028129a36616fa6edac8dad073ba676701bf5c6b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateTransition", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c998768bea3a09f4e7b233be09de600d2dda33cf13c5a3a084f0548bcb292723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)


@jsii.data_type(
    jsii_type="jira.issue.IssueConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "issue_type": "issueType",
        "project_key": "projectKey",
        "summary": "summary",
        "assignee": "assignee",
        "delete_transition": "deleteTransition",
        "description": "description",
        "fields": "fields",
        "id": "id",
        "labels": "labels",
        "reporter": "reporter",
        "state": "state",
        "state_transition": "stateTransition",
    },
)
class IssueConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        issue_type: builtins.str,
        project_key: builtins.str,
        summary: builtins.str,
        assignee: typing.Optional[builtins.str] = None,
        delete_transition: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        reporter: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        state_transition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param issue_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#issue_type Issue#issue_type}.
        :param project_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#project_key Issue#project_key}.
        :param summary: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#summary Issue#summary}.
        :param assignee: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#assignee Issue#assignee}.
        :param delete_transition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#delete_transition Issue#delete_transition}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#description Issue#description}.
        :param fields: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#fields Issue#fields}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#id Issue#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#labels Issue#labels}.
        :param reporter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#reporter Issue#reporter}.
        :param state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state Issue#state}.
        :param state_transition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state_transition Issue#state_transition}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22cd0e863226f1bd99ece89245bda87e3c30fbd7ef4e7bb1c22be8de6fe43a1b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument issue_type", value=issue_type, expected_type=type_hints["issue_type"])
            check_type(argname="argument project_key", value=project_key, expected_type=type_hints["project_key"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument assignee", value=assignee, expected_type=type_hints["assignee"])
            check_type(argname="argument delete_transition", value=delete_transition, expected_type=type_hints["delete_transition"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument reporter", value=reporter, expected_type=type_hints["reporter"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument state_transition", value=state_transition, expected_type=type_hints["state_transition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "issue_type": issue_type,
            "project_key": project_key,
            "summary": summary,
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
        if assignee is not None:
            self._values["assignee"] = assignee
        if delete_transition is not None:
            self._values["delete_transition"] = delete_transition
        if description is not None:
            self._values["description"] = description
        if fields is not None:
            self._values["fields"] = fields
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if reporter is not None:
            self._values["reporter"] = reporter
        if state is not None:
            self._values["state"] = state
        if state_transition is not None:
            self._values["state_transition"] = state_transition

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
    def issue_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#issue_type Issue#issue_type}.'''
        result = self._values.get("issue_type")
        assert result is not None, "Required property 'issue_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#project_key Issue#project_key}.'''
        result = self._values.get("project_key")
        assert result is not None, "Required property 'project_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def summary(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#summary Issue#summary}.'''
        result = self._values.get("summary")
        assert result is not None, "Required property 'summary' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignee(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#assignee Issue#assignee}.'''
        result = self._values.get("assignee")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_transition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#delete_transition Issue#delete_transition}.'''
        result = self._values.get("delete_transition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#description Issue#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fields(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#fields Issue#fields}.'''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#id Issue#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#labels Issue#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def reporter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#reporter Issue#reporter}.'''
        result = self._values.get("reporter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state Issue#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_transition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs/resources/issue#state_transition Issue#state_transition}.'''
        result = self._values.get("state_transition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IssueConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Issue",
    "IssueConfig",
]

publication.publish()

def _typecheckingstub__aef262c703edce4195e5912484af2c857cd26e1c45534dad7eb21e5e47c26e21(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    issue_type: builtins.str,
    project_key: builtins.str,
    summary: builtins.str,
    assignee: typing.Optional[builtins.str] = None,
    delete_transition: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    reporter: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    state_transition: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e9e9240e44b2c282573a4737a820163ad8423d27d47a08657d3e0c98bcaa4e49(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dbedaecf2c091e3dd00381bc632d8a19cd74a7098485daaec5edebf79ab6781(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a8663c0e9db70faf7e69770602f8fa7de2eab6b7f1e87045f03efeed647802(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfbb41b07a439e3bde9fa0ac3fde2071c2910449ceaf29afba7fb34f905b7c9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65f9028ed6be7459f608bc2a17494a29f1c03b36c66f898ca3c64b3b1df351c0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b4526e137d050737b4397d092afbd257a89ed2174cac4184db97ed8c3b0e54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b190f246aa6579fdaec04020d883c4512eec9b3881a9bdd45a03b7a5fa07de8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e331e3a2057a51546cba93c682553189d5838a63ddd3824438a068e7a30a9700(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ca0003d0e1dbba84af0a8acc84202c9f08271726abd939ccc5a5a787d3410c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536e4f2e01cecdb23b22747da63abe49b499840e44863f3fc56033995d6ef53c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c553e0a18b818d5bb7e4cc1eeb0004293b270247a4632449b30f8c79a30ecd09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2931ccff34eaacb52c1dd7a028129a36616fa6edac8dad073ba676701bf5c6b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c998768bea3a09f4e7b233be09de600d2dda33cf13c5a3a084f0548bcb292723(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22cd0e863226f1bd99ece89245bda87e3c30fbd7ef4e7bb1c22be8de6fe43a1b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    issue_type: builtins.str,
    project_key: builtins.str,
    summary: builtins.str,
    assignee: typing.Optional[builtins.str] = None,
    delete_transition: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    reporter: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    state_transition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
