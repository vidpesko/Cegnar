import { getHomePage } from "$lib/api/client.js";
import { getGallery } from "$lib/api/client";


export async function load() {
    return {
        home: await getHomePage(),
        gallery: await getGallery(true, 5),
    };
}