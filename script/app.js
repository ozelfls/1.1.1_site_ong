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

const bannerSlides = document.querySelectorAll('.bannerSlide');
const dots = document.querySelectorAll('.dot');
let atualIndex = 0;
let intervalo;

function showSlide(index) {
  bannerSlides.forEach((slide, i) => {
    slide.classList.toggle('ativo', i === index);
    const fill = dots[i].querySelector('.preencher');
    fill.style.transition = 'none';
    fill.style.width = '0%';
    if (i === index) {
      void fill.offsetWidth;
      fill.style.transition = 'width 5s linear';
      fill.style.width = '100%';
    }
  });
  atualIndex = index;
}

function proximoSlide() {
  showSlide((atualIndex + 1) % bannerSlides.length);
}

function iniciarCarrossel() {
  clearInterval(intervalo);
  intervalo = setInterval(proximoSlide, 5000);
  showSlide(atualIndex);
}

dots.forEach((dot, i) => {
  dot.addEventListener('click', () => {
    showSlide(i);
    iniciarCarrossel();
  });
});

iniciarCarrossel();

let contadorSecreto = 0;
const botao = document.getElementById('botaoMagico')
const link = document.getElementById('linkSecreto')

botao.addEventListener('click', () => {
    contadorSecreto++;
    if(contadorSecreto === 3) {
        link.classList.add('aparecer');
    }
});
