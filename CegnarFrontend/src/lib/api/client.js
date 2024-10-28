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
    let response = await get("/pages?type=home.HomePage&fields=*");
    return response;
}

export async function getExperiences() {
    let url = BASE_PATH + "/list-experiences/";

    const response = await fetch(url);

    if (!response.ok) {
        return {
            error: response.status
        }
    }

    return await response.json();
}