import { getHomePage } from "$lib/api/client.js";


export async function load() {
    return {
        home: await getHomePage(),
    };
}