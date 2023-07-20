import React from 'react';
import { Container, Navbar } from 'react-bootstrap';

const Footer = () => {
    return (
        <Navbar fixed="bottom" bg="light">
            <Container>
                <Navbar.Text>
                    Hack GPT
                </Navbar.Text>
            </Container>
        </Navbar>
    );
}

export default Footer;
