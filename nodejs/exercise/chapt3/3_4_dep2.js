const dep1 = require('./3_4_dep1');
console.log('require dep1', dep1);
module.exports = () => {
  console.log('dep1', dep1);
}