import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './Components/home/home';
import SignIn from './Components/sign_in/sign_in';
import GoogleCalendar from './Components/home_GoogleCalendar/home_GoogleCalendar'
import GoogleMeet from './Components/home_GoogleMeet/home_GoogleMeet'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sign_in" element={<SignIn />} />
        <Route path="/home_GoogleCalendar" element={<GoogleCalendar />} />
        <Route path="/home_GoogleMeet" element={<GoogleMeet />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
