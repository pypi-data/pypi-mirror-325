'''
# `provider`

Refer to the Terraform Registry for docs: [`jira`](https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs).
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


class JiraProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="jira.provider.JiraProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs jira}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs jira} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param url: URL for your Jira instance. Can be specified with the JIRA_URL environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#url JiraProvider#url}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#alias JiraProvider#alias}
        :param password: Password for the user, can also be an API Token. Can be specified with the JIRA_PASSWORD environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#password JiraProvider#password}
        :param token: Personal access token of a user. Can be specified with the JIRA_TOKEN environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#token JiraProvider#token}
        :param user: Username for your user. Can be specified with the JIRA_USER environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#user JiraProvider#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec756f816bb836fcb338e7c3d38b7c7babd1f7f2daaf536ac7bcece5e6d0d49)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = JiraProviderConfig(
            url=url, alias=alias, password=password, token=token, user=user
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
        '''Generates CDKTF code for importing a JiraProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the JiraProvider to import.
        :param import_from_id: The id of the existing JiraProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the JiraProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2be3cb5bf179362b03d4c538b26f277ae4d546ac45a5e6cdaa02bc028a74cf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5765a9cd18429ba9a4837eae1cfa855797548e3824030574a211bfca48575a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__278af251bdd737bd5fa5c9a318da20f6d2df261667856305ab92a0e9a88e8fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b37c0f970a9b196e9093832413506fb7f7587e918dec05b6bd06b477a30133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf9ad545e9b667d08c78f643580ea2acae4644e07dca50e82a05f1c3d27ad55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "user"))

    @user.setter
    def user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d6a5a46cc405cf337e6ed4c893509969eeb9124ff201d29df6c37d3aecbe08a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)


@jsii.data_type(
    jsii_type="jira.provider.JiraProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "alias": "alias",
        "password": "password",
        "token": "token",
        "user": "user",
    },
)
class JiraProviderConfig:
    def __init__(
        self,
        *,
        url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: URL for your Jira instance. Can be specified with the JIRA_URL environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#url JiraProvider#url}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#alias JiraProvider#alias}
        :param password: Password for the user, can also be an API Token. Can be specified with the JIRA_PASSWORD environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#password JiraProvider#password}
        :param token: Personal access token of a user. Can be specified with the JIRA_TOKEN environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#token JiraProvider#token}
        :param user: Username for your user. Can be specified with the JIRA_USER environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#user JiraProvider#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cdfc8e03e40dae6d12121fe67128944660ac61dd154c87373ed5de1558b617)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if alias is not None:
            self._values["alias"] = alias
        if password is not None:
            self._values["password"] = password
        if token is not None:
            self._values["token"] = token
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def url(self) -> builtins.str:
        '''URL for your Jira instance. Can be specified with the JIRA_URL environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#url JiraProvider#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#alias JiraProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for the user, can also be an API Token. Can be specified with the JIRA_PASSWORD environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#password JiraProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Personal access token of a user. Can be specified with the JIRA_TOKEN environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#token JiraProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''Username for your user. Can be specified with the JIRA_USER environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/fourplusone/jira/0.1.20/docs#user JiraProvider#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JiraProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "JiraProvider",
    "JiraProviderConfig",
]

publication.publish()

def _typecheckingstub__aec756f816bb836fcb338e7c3d38b7c7babd1f7f2daaf536ac7bcece5e6d0d49(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2be3cb5bf179362b03d4c538b26f277ae4d546ac45a5e6cdaa02bc028a74cf6(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5765a9cd18429ba9a4837eae1cfa855797548e3824030574a211bfca48575a25(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__278af251bdd737bd5fa5c9a318da20f6d2df261667856305ab92a0e9a88e8fe8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b37c0f970a9b196e9093832413506fb7f7587e918dec05b6bd06b477a30133(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf9ad545e9b667d08c78f643580ea2acae4644e07dca50e82a05f1c3d27ad55(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6a5a46cc405cf337e6ed4c893509969eeb9124ff201d29df6c37d3aecbe08a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cdfc8e03e40dae6d12121fe67128944660ac61dd154c87373ed5de1558b617(
    *,
    url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
