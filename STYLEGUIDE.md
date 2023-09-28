# Code Style Guide

A lot of this guide is inspired by https://airbnb.io/javascript/react/

## File Organization

All components should be in their own directories. The directory name should be
the name of the component. The component should be implemented in `index.jsx`,
and styles should be applied through classes that refer to styles specified in
`styles.js`, in the same directory. As an example, MyComponent is implemented as
such:

```
- MyComponent
    - index.jsx
    - styles.js
```

By putting the component in `index.jsx`, you can import it with shorter syntax:

`import MyComponent from './MyComponent';`

instead of

`import MyComponent from './MyComponent/MyComponent';`

Components should be created in `.jsx` files. Other files, specific for logic
and styles and such, should be in a `.js` file.

Also note that we use PascalCase to name components. However, when creating a
reference to the component, the variable should be named in camelCase so it is
clear what is what. As an example:

`const myComponent = MyComponent`

## Linting:

Most style issues can be handled with the proper linting extensions in VS Code.
For this project, we are using
[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
and
[ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint).

Some key points:

- double quotes instead of single quotes
- child components should be indented
- uh

## React Guidelines

Functional components only. No class components.

Example of functional component (good!):

```
const Car = () => {
    return <h2>Hi, I am also a Car!</h2>;
}
```

Example of class component (bad!):

```
class Car extends React.Component {
    render() {
        return <h2>Hi, I am a Car!</h2>;
    }
}
```

For simplicity's sake, we use arrow functions for all components instead of
normal functions.

Example of arrow function (good):

```
const add = (num1, num2) => {
    return num1 + num2;
}
```

Example of normal function (bad):

```
function add(num1, num2) {
    return num1 + num2;
}
```

### Params

Pass in parameters as an object if there are more than 5 props being passed into
a component:

```
const myComponentProps = {
    prop1,
    prop2,
    prop3: "Hello",
    prop4,
    prop5: "World",
    prop6
};

<MyComponent {...myComponentProps}>
```

Props should be in camelCase.

If possible, keep the component in one line. If it overflows, the params should
be in a different line as such:

```
<Foo
  superLongParam="bar"
  anotherSuperLongParam="baz"
/>
```

### Imports

If there are a lot of imports in a component, split them into 3 sections:

- External Libraries
  - `import { useState } from "react"`
- Absolute paths
  - `import { CustomComponent } from "ui-components/core"`
- Relative paths
  - `import { useStyles } from "./styles.js"`

The sections should have 1 line of whitespace between them for better clarity.

If you have a singular component that stands by itself, export it directly as
such:

`export default MyComponent;`

So you can import it without braces:

`import MyComponent from "MyComponent/index.jsx"`

If you're compiling a library or group of components that fall within the same
directory, export each one within its file, but create an overarching `index.js`
where you import all of the components, and then export them in a group within
braces.

```
import ComponentOne from "./ComponentOne/index.jsx";
import ComponentTwo from "./ComponentTwo/index.jsx";
import ComponentThree from "./ComponentThree/index.jsx";

export {
    ComponentOne,
    ComponentTwo,
    ComponentThree
};
```

This way, when you go to import one of the components, it's intuitively
formatted as if it were part of a library.

`import { ComponentTwo } from "MyComponents"`

Functions should always be exported and imported within braces {}

`import { useStyles } from "./styles.js`

## Accessibility

[ARIA roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques)
should be a real Aria role and describe the component generally.

```
// bad - not an ARIA role
<div role="datepicker" />

// bad - too specific
<div role="cancel-button" />

// good
<div role="button" />
```
