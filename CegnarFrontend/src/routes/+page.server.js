import { getHomePage, getGallery } from "$lib/api/client.js";


export async function load() {
    return {
        home: await getHomePage(),
        gallery: await getGallery({
            onlyImg: true,
            limit: 5,
        }),
    };
}