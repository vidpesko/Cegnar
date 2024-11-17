const BASE_PATH = "https://cegnarblacksmithing.com/backend/api";

async function get(path) {
    let url = BASE_PATH + path;

    try {
        const response = await fetch(url);
    } catch (error) {
        return {
            error
        }
    }

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

export async function getGallery({
    onlyImg = false,
    category = null,
    limit = 0,
} = {}) {
    let path = "/pages/6?";
    
    if (onlyImg) {
        path = "/product/?";
    }
    
    if (category) {
        path = "/product/?category=" + category + "&";
    }

    if (limit !== 0) {
        path = path + "limit=" + String(limit) + "&";
    }

    let response = await get(path);
    return response;
}

export async function getSpecificProduct(id) {
    let response = await get("/product/" + id);
    return response;
}

export async function getSettings() {
    let response = await get("/settings/personal/");
    return response;
}

export async function getProductCategories() {
    let response = await get("/product/categories/");
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


export async function postMessage({
    name,
    email,
    contact_reason = "",
    product_model = "",
    message = ""
} = {}) {
    let url = BASE_PATH + "/contact/message/";

    const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({ name, email, contact_reason, product_model, message }),
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (!response.ok) {
        return {
            error: response.status
        };
    }

    return await response.json();
}