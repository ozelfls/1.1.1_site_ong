window.addEventListener("scroll", () =>{
    const header = document.getElementById("header-top");
    const logoCasa = document.getElementById("casaRaraLogo");
     if(window.scrollY > 20){
        header.classList.add("colorHeader")
        logoCasa.src = './imagens/casa_rara.png'
    }else{
        header.classList.remove("colorHeader")
        logoCasa.src = './imagens/casaRaraBranco_1.png'
    }
})

const slides = document.querySelectorAll('.slide');
  let indexAtual = 0;

  function mostrarSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.remove('ativa');
      if (i === index) slide.classList.add('ativa');
    });
  }

  function mudarSlide(direcao) {
    indexAtual += direcao;
    if (indexAtual < 0) indexAtual = slides.length - 1;
    if (indexAtual >= slides.length) indexAtual = 0;
    mostrarSlide(indexAtual);
  }
  
  mostrarSlide(indexAtual);

  function copiarChavePix() {
    const chavePix = 'casa.atipicaa@gmail.com';
    const botao = document.getElementById('copiarPix');

    navigator.clipboard.writeText(chavePix).then(() => {
        botao.textContent = 'Copiado!';
        botao.disabled = true;

        setTimeout(() => {
            botao.textContent = 'Copiar Chave';
            botao.disabled = false;
        }, 2000);
    }).catch(err => {
        console.error('Erro ao copiar: ', err);
    });
}