import React, { useEffect, useState } from "react";
import "./Usuario.css";
import usuarioPrimario from "../imagens/usuarioPrimario.png"

export default function Usuario() {
    const [data, setData] = useState([]); // Define o estado inicial como um array vazio
    const [error, setError] = useState(null); // Estado para erros
    const [loading, setLoading] = useState(true); // Estado para carregamento

    useEffect(() => {
        // Faz a chamada para a API
        fetch("http://127.0.0.1:5000/usuarios") // URL do backend
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
                console.error("Erro ao buscar dados:", error);
                setError(error.message); // Define o erro no estado
            })
            .finally(() => setLoading(false)); // Finaliza o carregamento
    }, []);

    return (
        <>
            <h1>Usuários</h1>
            {loading && <p>Carregando...</p>} {/* Exibe enquanto está carregando */}
            {error && <p style={{ color: "red" }}>Erro: {error}</p>} {/* Exibe erro, se houver */}
            <div>
                <h2>Conheça nossos usuários!</h2>
                <img src={usuarioPrimario} alt="" />
                <ul className="usuarios-list">
                    {data.length > 0 ? (
                        data.map((item, index) => (
                            <li key={index} className="usuarios-item">
                                {Object.entries(item).map(([key, value]) => (
                                    <div key={key} className="usuarios-detail">
                                        <span className="usuarios-key">{key}:</span>
                                        <span className="usuarios-value">{value}</span>
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
