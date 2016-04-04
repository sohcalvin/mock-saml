
class OneLogin_Saml2_Auth:

  def __init__(self,request, custom_base_path=None):
      pass


  def login(self,ret_to=None):
      return "/login"

  def logout(self, name_id=None, session_index=None) :
      return "/logout"

  def process_response(self) :
      pass

  def is_authenticated(self) :
      pass

  def get_attributes(self) :
      pass

  def get_nameid(self) :
      pass

  def get_session_index(self) :
      pass

  def redirect_to(self, relay_state) :
      pass

  def process_slo(self, delete_session_cb=None) :
      pass

  def get_errors(self) :
      pass

  def get_settings() :
      pass