import GoogleLogin from "react-google-login";

const clientId = '856817536355-vpaqv9k121ko0dfhdhrt2krsr6uo97g4.apps.googleusercontent.com';

function Login({ onSuccess }) {

    const onSuccess =(res)=>{
        console.log("LOGIN SUCCESS! Current user :" , res.profileObj);
    }

    const onFailure = (res) => {
        console.log("LOGIN Failed! res:", res);
    }


    return (
        <div id="signInButton">
            <GoogleLogin
                clientId={clientId}
                buttonText="Login"
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                isSignedIn={true}
            />
        </div>
    )
}

export default Login