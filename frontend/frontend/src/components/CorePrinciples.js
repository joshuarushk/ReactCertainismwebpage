import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CorePrinciples = () => {
    const [principles, setPrinciples] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/core-principles/')
            .then(response => setPrinciples(response.data.principles))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Core Principles</h2>
            <ul>
                {principles.map((principle, index) => (
                    <li key={index}>{principle}</li>
                ))}
            </ul>
        </div>
    );
};

export default CorePrinciples;
