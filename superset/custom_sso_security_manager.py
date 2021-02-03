import logging
import os

from superset import SupersetSecurityManager

logger = logging.getLogger(__name__)


class CustomSsoSecurityManager(SupersetSecurityManager):

    def auth_user_oauth(self, userinfo):
        """
            OAuth user Authentication

            :userinfo: dict with user information the keys have the same name
            as User model columns.
        """
        # Search for the user by email to support existing users logging in via their Google Account
        if "email" in userinfo:
            user = self.find_user(email=userinfo["email"])
        else:
            logger.error("User info does not have username or email {0}".format(userinfo))
            return None
        # User is disabled
        if user and not user.is_active:
            from flask_appbuilder.const import LOGMSG_WAR_SEC_LOGIN_FAILED
            logger.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(userinfo))
            return None
        # If user does not exist on the DB and not self user registration, go away
        if not user and not self.auth_user_registration:
            return None
        # User does not exist, create one if self registration.
        if not user:
            role_name = self.auth_user_registration_role
            print()
            if self.auth_user_registration_role_jmespath:
                import jmespath

                role_name = jmespath.search(
                    self.auth_user_registration_role_jmespath, userinfo
                )
            user = self.add_user(
                username=userinfo["username"],
                first_name=userinfo.get("first_name", ""),
                last_name=userinfo.get("last_name", ""),
                email=userinfo.get("email", ""),
                role=self.find_role(role_name),
            )
            if not user:
                logger.error("Error creating a new OAuth user %s" % userinfo["username"])
                return None
        self.update_user_auth_stat(user)
        return user
