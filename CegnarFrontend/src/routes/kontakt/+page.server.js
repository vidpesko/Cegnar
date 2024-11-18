import { getContactPage, getProductCategories, postMessage } from "$lib/api/client";


export async function load() {
    return {
        contact: await getContactPage(),
        categories: await getProductCategories(),
    };
}

export const actions = {
    default: async ({ cookies, request }) => {
        // Get data
        const data = await request.formData();

        // Send api request with data
        let response = await postMessage({
            name: data.get("name"),
            email: data.get("email"),
            contact_reason: data.get("contact-reason"),
            contact_reason: data.get("product-type") || "",
            message: data.get("message") || "",
        });

        if (response.error) {
            return {
                success: false,
            };
        } else {
            return {
                success: true,
            };
        }
    }
};