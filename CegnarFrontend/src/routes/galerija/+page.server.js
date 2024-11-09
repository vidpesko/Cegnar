import { getGallery, getProductCategories } from "$lib/api/client";


export async function load() {
    return {
        page: await getGallery(),
        categories: await getProductCategories(),
    };
}
