import { GoogleLogin, GoogleOAuthProvider } from '@react-oauth/google';
import { jwtDecode } from "jwt-decode";


function SignIn() {
  return (
    <GoogleOAuthProvider clientId="856817536355-vpaqv9k121ko0dfhdhrt2krsr6uo97g4.apps.googleusercontent.com">
      <GoogleLogin
          onSuccess={credentialResponse => {
            const credentialResponseDecoded = jwtDecode(credentialResponse.credential);
            console.log(credentialResponseDecoded);
          }}
          onError={() => {
            console.log('Login Failed');
          }}
      />
    </GoogleOAuthProvider>
    
  );
}

export default SignIn;