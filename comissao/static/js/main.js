//  //inicio função envio do cargo para div cargos//
//
// const btn = document.querySelector('#confirmar_cargo');
//
//       confirmar_cargo.addEventListener("click" ,function(e) {
//
//         e.preventDefault();
//
//         const check = document.querySelector(".listCargos");
//
//         const value = check.value;
//
//         // let checkbox = document.getElementById('cargo');
//         if (check.checked) {
//             document.getElementById("nome_cargo").innerHTML = value;
//         } else {
//             alertWarning("Selecione um Cargo");
//         }
//         });
//
//  //fim função envio do cargo para div cargos//
//
//  //Inicio função desabilitar checks//
//
// (function (){
//     "use strict";
//
//     let marcado = 0;
//     let verificarcheck = function ($checks) {
//         if (marcado > 0 ) {
//             loop($checks, function($element){
//                 $element.disabled = $element.checked ? '' : 'disabled';
//             });
//         } else {
//             loop($checks, function($element){
//                 $element.disabled = '';
//             });
//         }
//     };
//
//     let loop = function($element, cb){
//         let max = $element.length;
//         while(max--) {
//             cb($element[max]);
//         }
//     }
//     let count = function($element){
//         return $element.checked ? marcado + 1 : marcado - 1;
//     }
//
//     window.onload = function(){
//         let $checks = document.querySelectorAll('.listCargos');
//         loop($checks, function($element){
//             $element.onclick = function(){
//                 marcado = count(this);
//                 verificarcheck($checks);
//             }
//             if($element.checked) marcado = marcado + 1;
//         });
//
//         verificarcheck($checks);
//     }
// }());
//
// //Fim função desabilitar checks//

// window.onload = function(){
//     let checkbox = document.querySelectorAll(".listCargos");
//     loop(checkbox, function (el){
//
//     })
// }
//
//
// loop()
//
// checkbox.addEventListener('click', function (){
//     if (this.checked){
//         alert('check')
//     }else{
//         alert('no check')
//     }
// })

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

    // if (el.checked){
    //     alert('check')
    // }else{
    //     alert('no check')
    // }
}