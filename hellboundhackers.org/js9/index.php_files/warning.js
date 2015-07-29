var node = new Element("div", {className: "warning", style: "display:none"}).update(
  new Element('p').update('Are you sure to delete this item?')
).insert(
  new Element("input", {type: "button", value: "Yes, delete it!", id: "deleteBut"})
).insert(
  new Element('span').update(' or ')
).insert(
  new Element("input", {type: "button", value: "No, leave it", id: "cancelBut"})
);

function setObservers ()
{
  $('deleteBut').observe('click', Modalbox.hide.bindAsEventListener(Modalbox));
  $('cancelBut').observe('click', Modalbox.hide.bindAsEventListener(Modalbox));
}
function removeObservers ()
{
  $('deleteBut').stopObserving('click', Modalbox.hide.bindAsEventListener(Modalbox));
  $('cancelBut').stopObserving('click', Modalbox.hide.bindAsEventListener(Modalbox));
}