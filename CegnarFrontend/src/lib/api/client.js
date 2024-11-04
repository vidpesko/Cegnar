const BASE_PATH = "http://localhost:8000/api";


async function get(path) {
    let url = BASE_PATH + path;

    const response = await fetch(url);

    if (!response.ok) {
        return {
            error: response.status
        };
    }

    return await response.json();
}

export async function getHomePage() {
    let response = await get("/pages/3/?fields=*");
    return response;
}

export async function getGallery(onlyImg=false, limit=0) {
    let path = "/pages/6?";
    if (limit !== 0) {
        path = path + "limit=" + String(limit) + "&";
    }

    if (onlyImg) {
        path = path + "fields=gallery_images";
    }

    let response = await get(path);
    return response;
}

export async function getSettings() {
    let response = await get("/settings/personal/");
    return response;
}

export async function getContactPage() {
    let response = await get("/pages/5/?fields=*");
    return response;
}

export async function getAboutPage() {
    let response = await get("/pages/4/?fields=*");
    return response;
}
