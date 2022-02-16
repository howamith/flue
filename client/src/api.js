/**
 * Retrieve some JSON from an API endpoint.
 * 
 * @param {string} endpoint The endpoint the retrieve the JSON from.
 * @returns {Object} The JSON retrieved from the endpoint, deserialised into an
 *   object.
 */
export async function getJson(endpoint) {
  return await _makeRequest({ endpoint });
}

/**
 * Post some JSON to an API endpoint.
 * @param {string} endpoint The API to post the JSON to.
 * @param {Object} json The object to serialise (as JSON) and post.
 * @returns {Object} The response JSON received from the server.
 */
export async function postJson(endpoint, json) {
  return await _makeRequest({
    endpoint, method: "POST", body: json, contentType: "application/json"
  });
}

/**
 * Make a request to an API endpoint.
 * 
 * @param {Object} opts - The options for making the request.
 * @param {string} opts.endpoint - The API endpoint to make the request to.
 * @param {string=} opts.method - The type of HTTP request to make ("GET" by
 *   default).
 * @param {Object=} opts.body - The body to send in the request, which will be
 *   serialised as JSON.
 * @param {string=} opts.body - The request's body's content type.
 * @returns {Object} The response's body, deserialised as JSON into an object.
 */
async function _makeRequest(
  { endpoint, method = "GET", body = null, contentType = null }
) {
  // Setup Fetch API options.
  const opts = { method, headers: {} };
  if (body !== null) {
    opts.body = JSON.stringify(body);
  }
  if (contentType !== null) {
    opts.headers["Content-Type"] = contentType;
  }

  // Perform the request and ensure the server didn't respond with an error.
  const response = await fetch(endpoint, opts);
  if (!response.ok) {
    throw new Error("Failed to start task.");
  }

  // Extract JSON body from the response.
  try {
    return await response.json();
  } catch (error) {
    throw new Error("Failed to parse task response:" + error);
  }
}