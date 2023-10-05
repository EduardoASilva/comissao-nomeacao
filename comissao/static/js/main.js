function checkbox(el){
    let checkbox = document.querySelectorAll(".listCargos");

    if (el.checked){
        for (const check of checkbox){
            if (!check.checked){
                check.disabled = true
            }
        }
    }else{
        for (const check of checkbox){
            check.disabled = false
        }
    }

    let cargo = 'Cargo';
    let nome_cargo = $('#nome_cargo')[0];
    if (nome_cargo.innerText !== cargo){
        nome_cargo.innerText = cargo
    }
}