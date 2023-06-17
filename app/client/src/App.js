import React from 'react';
import { Container } from 'react-bootstrap';
import NavBar from './components/NavBar';
import Footer from './components/Footer';

function App() {
    return (
        <div>
            <NavBar />
            <Container>
                <h1>Welcome to the Homepage!</h1>
                <p>This is some basic structure for the homepage.</p>
            </Container>
            <Footer />
        </div>
    );
}

export default App;