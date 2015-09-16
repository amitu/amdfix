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
import require dojo/on;

domClass.add(document.body, "dojorocks");
on(window, "resize", function(){

});

function foo() {

}

export foo;
```
