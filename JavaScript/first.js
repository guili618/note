var s = 6
var l = '12'
console.log(s + l)

function add(a, b) {
    return a + b;

}
console.log(add(3, 4))
Array a1 = [1, 2, 3, 4]

function createNewPerson(name) {
    var obj = {};
    obj.name = name;
    obj.greeting = function() {
        console.log('Hi! I\'m ' + this.name + '.');
    };
    return obj;
}

var salva = createNewPerson('Salva');
console.log(salva.name);
salva.greeting();