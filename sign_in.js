// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyDP7fO5FPOPwswJGqVVqD-eoY40G3Xl2_E",
  authDomain: "primordial-veld-423001-g5.firebaseapp.com",
  projectId: "primordial-veld-423001-g5",
  storageBucket: "primordial-veld-423001-g5.appspot.com",
  messagingSenderId: "856817536355",
  appId: "1:856817536355:web:4c14bbc86dd503b62e5756",
  measurementId: "G-5GSDE2GHJD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
auth.languageCode = 'en';
const provider = new GoogleAuthProvider();

const googleLogin = document.getElementById("google-login-btn")
googleLogin.addEventListener("click", function(){
    signInWithPopup(auth, provider)
        .then((result) => {
            const credential = GoogleAuthProvider.credentialFromResult(result);
            const user = result.user;
            window.location.href = "";
        }).catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
        })
})
const analytics = getAnalytics(app);