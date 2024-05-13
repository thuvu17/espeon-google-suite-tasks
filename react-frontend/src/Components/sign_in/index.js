import React from 'react';
import ReactDOM from 'react-dom';
import { GoogleOAuthProvider } from '@react-oauth/google';
import SignIn from './sign_in.jsx';

ReactDOM.createroot(document.getElementById("root").render(
    <React.StrictMode>
        <GoogleOAuthProvider clientId="856817536355-vpaqv9k121ko0dfhdhrt2krsr6uo97g4.apps.googleusercontent.com">
            <SignIn />
    </GoogleOAuthProvider>,
    </React.StrictMode>
)) ;