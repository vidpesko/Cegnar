import { getGallery } from "$lib/api/client";


export async function load() {
    return {
        page: await getGallery(),
    };
}
