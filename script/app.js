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