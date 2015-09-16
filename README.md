Instead of writing

```javascript
define(["dojo/dom-class", "dojo/on"], function(domClass, on){
	domClass.add(document.body, "dojorocks");
	on(window, "resize", function(){

	});

	function foo() {

	}

	return foo;
});
```

Write

```javascript
import dojo/dom-class;
// above is same as: import dojo/dom-class as domClass;
import dojo/on;

domClass.add(document.body, "dojorocks");
on(window, "resize", function(){

});

function foo() {

}

export foo;
```
