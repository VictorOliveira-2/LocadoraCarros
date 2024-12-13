import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Carousel } from 'react-bootstrap'; // Importando o componente Carousel
import 'bootstrap/dist/css/bootstrap.min.css'; // Estilo necessário para o Bootstrap

import Alugados from './components/Alugados.jsx';
import Menu from './components/Menu.jsx';
import Carros from './components/Carros.jsx';
import Usuario from './components/Usuario.jsx';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import ronaldinhoCarrosel from "./imagens/ronaldinhoCarrosel.jpeg";
import carroCarrosel from "./imagens/carroCarrosel.jpeg";

function App() {
  return (
    <>
      <Header />
      <Router>
        <Menu />
        <div className="page-content">
          <Routes>
            <Route
              path="/"
              element={
                <>
                  <h2>Bem-vindo à Localize!</h2>
                  <Carousel fade className="home-carousel">
                    <Carousel.Item>
                      <img
                        className="d-block w-100"
                        src={ronaldinhoCarrosel}
                        alt="Primeira Fase"
                      />
                      <Carousel.Caption>
                        <h3></h3>
                        <p>Faça como nosso craque, drible a concorrência!</p>
                      </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                      <img
                        className="d-block w-100"
                        src={carroCarrosel}
                        alt="Fase"
                      />
                      <Carousel.Caption>
                        <p>Seja parte da nossa comunidade como cliente VIP!</p>
                      </Carousel.Caption>
                    </Carousel.Item>
                  </Carousel>
                  <br></br>
                  <p>
                    <strong>Sobre a LocalizE:</strong><br />
                    Bem-vindo à LocalizE, a solução completa para quem busca mobilidade com conforto, segurança e praticidade. Somos uma empresa inovadora no setor de aluguel de veículos, dedicada a transformar sua experiência de locomoção, seja para viagens de lazer, negócios ou necessidades do dia a dia.<br /><br />

                    Com uma ampla frota de veículos modernos e bem mantidos, a LocalizE oferece opções para todos os perfis: desde compactos econômicos até SUVs luxuosos e utilitários versáteis. Trabalhamos com transparência e compromisso para garantir que você tenha um serviço de alta qualidade e sem complicações.<br /><br />

                    Nosso diferencial está em unir tecnologia de ponta a um atendimento humanizado. Por meio de nossa plataforma digital, você pode reservar seu veículo de forma rápida e intuitiva, escolhendo o modelo ideal para sua necessidade. Além disso, contamos com diversas opções de planos e preços competitivos, garantindo a melhor relação custo-benefício.
                  </p>

                  <div className="por-que-escolher">
                    <div>
                      <h3>Frota diversificada</h3>
                      <p>Veículos para todos os estilos e ocasiões.</p>
                    </div>
                    <div>
                      <h3>Facilidade de reserva</h3>
                      <p>Reserve online ou em nossas unidades físicas.</p>
                    </div>
                    <div>
                      <h3>Suporte 24/7</h3>
                      <p>Atendimento ágil para ajudá-lo em qualquer situação.</p>
                    </div>
                    <div>
                      <h3>Sustentabilidade</h3>
                      <p>Investimos em veículos elétricos e híbridos.</p>
                    </div>
                  </div>

                  <p>
                    Na LocalizE, nosso objetivo é mais do que oferecer um serviço de aluguel de carros. Queremos proporcionar liberdade, autonomia e a melhor experiência de viagem para nossos clientes.<br /><br />

                    <strong>Escolha a LocalizE</strong> e descubra como é simples, rápido e confiável alugar um carro com quem entende de mobilidade!
                  </p>
                </>
              }
            />
            <Route path="/Carros" element={<Carros />} />
            <Route path="/Alugados" element={<Alugados />} />
            <Route path="/Usuario" element={<Usuario />} />
          </Routes>
        </div>
      </Router>
      <Footer />
    </>
  );
}

export default App;
