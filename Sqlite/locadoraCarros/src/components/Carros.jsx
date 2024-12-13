import React, { useEffect, useState } from 'react';
import "./Carros.css";
import carroPrimario from "../imagens/carroPrimario.png";
export default function Carros() {
    const [data, setData] = useState([]); // Define o estado inicial como um array vazio
    const [error, setError] = useState(null); // Estado para erros
    const [loading, setLoading] = useState(true); // Estado para carregamento

    useEffect(() => {
        // Faz a chamada para a API
        fetch('http://127.0.0.1:5000/carros') // URL do backend
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`Erro: ${response.status}`); // Lança erro para status de resposta não OK
                }
                return response.json();
            })
            .then((json) => {
                setData(json); // Define os dados no estado
                setError(null); // Limpa erros
            })
            .catch((error) => {
                console.error('Erro ao buscar dados:', error);
                setError(error.message); // Define o erro no estado
            })
            .finally(() => setLoading(false)); // Finaliza o carregamento
    }, []);

    return (
        <>
            <h1>Carros</h1>
            {loading && <p>Carregando...</p>} {/* Exibe enquanto está carregando */}
            {error && <p style={{ color: 'red' }}>Erro: {error}</p>} {/* Exibe erro, se houver */}
            <div>
                <h2>Conheça nossos carros!</h2>
                <img src={carroPrimario} alt="" />
                <ul className="carros-list">
                    {data.length > 0 ? (
                        data.map((item, index) => (
                            <li key={index} className="carro-item">
                                {Object.entries(item).map(([key, value]) => (
                                    <div key={key} className="carro-detail">
                                        <span className="carro-key">{key}:</span>
                                        <span className="carro-value">{value}</span>
                                    </div>
                                ))}
                            </li>
                        ))
                    ) : (
                        !loading && <p>Nenhum dado encontrado.</p> // Exibe mensagem se a lista estiver vazia
                    )}
                </ul>
            </div>
        </>
    );
}