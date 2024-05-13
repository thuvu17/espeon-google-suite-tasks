import { GoogleOAuthProvider } from '@react-oauth/google';

root.render(
    <React.StrictMode>
      <GoogleOAuthProvider clientId="856817536355-vpaqv9k121ko0dfhdhrt2krsr6uo97g4.apps.googleusercontent.com">
        <ChakraProvider>
          <App />
        </ChakraProvider>
      </GoogleOAuthProvider>
    </React.StrictMode>,
  );