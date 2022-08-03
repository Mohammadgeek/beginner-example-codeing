//remove item

document.querySelector('#div-1').remove()
document.querySelector('#div-1').parentElement.remove()

/* 
if you are remove last child from div 
*/

function removelist(){
  const list = document.getElementById("div-2");
  if (list.hasChildNodes()){
    list.removeChild(list.lastChild);
  }
}
