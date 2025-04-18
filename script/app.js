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