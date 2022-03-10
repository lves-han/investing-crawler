function random_string(a) {
    var g = 'abcdefghijklmnopqrstuvwxyz0123456789_';
    b = g.length;
    var c,
        d = [];
    for (c = 0; c < a; c++) {
        d.push(g.substr(Math.floor(Math.random() * b), 1))
    };
    return d.join('')
}
console.log(random_string(8))