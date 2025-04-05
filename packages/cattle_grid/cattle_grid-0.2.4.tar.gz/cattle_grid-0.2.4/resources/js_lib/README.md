# cattle_grid account api sdk

The aim here is to create a client sdk for the cattle
grid account api.

## Usage

Import the relevant methods and configure the client with
the `baseUrl`.

```js
import { signin, accountInfo } from "./src";
import { client } from "./src/client.gen";

client.setConfig({
  baseUrl: "http://localhost:3001/fe",
});
```

### Signin

One can sign in into an account with the account name and the
corresponding password. For further requests, you will need the
bearer token.

```js
let result = await signin({ body: { name: "js", password: "js" } });

const bearerToken = result.data.token;
```

### Setting the bearer token

This is done via:

```js
client.interceptors.request.use(async (request) => { 
  request.headers.set("Authorization", "Bearer " + bearerToken);
  return request;
});
```

### Getting account info

This can be done via

```js
const result = await accountInfo();
```

The response data is in `result.data` the status code
can be retrieved from `result.response.status`.

Furthermore methods can be discovered via `sdk.gen`.
