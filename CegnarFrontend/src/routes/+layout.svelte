<script>
    // Custom css
    import "../app.css";
    // Splide js css
    import '@splidejs/svelte-splide/css';
    // Icons
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
    import PhoneIcon from '~icons/mdi/phone';
    import MapMarkerIcon from '~icons/mdi/map-marker';

    export let data;
    let settings = data.settings;
</script>

<slot />

<!-- Footer -->
<footer class="bg-background text-white border-t-[0.5px] relative">
    <div class="w-4/6 mx-auto">
        <!-- Columns -->
        <div class="pt-10 pb-4 md:flex-row flex flex-col justify-between items-start gap-8">
            <!-- 1. column - title, navigation -->
            <div class="footer-column">
                <div class="">
                    <h3 class="">Povezave</h3>
                </div>
                <ul>
                    <li><a href="/">Domov</a></li>
                    <li><a href="/galerija">Galerija</a></li>
                    <li><a href="/zgodba">Zgodba</a></li>
                    <li><a href="/kontakt">Kontakt</a></li>
                </ul>
            </div>
            <!-- 2. column - contact, home address -->
            <div class="footer-column">
                <div class="">
                    <h3>Kontakt</h3>
                </div>
                <ul>
                    <li>
                        <PhoneIcon />
                        <a href="tel:{settings.phone_number}">
                            {settings.phone_number}
                        </a>
                    </li>
                    <li>
                        <EmailIcon />
                        <a href="mailto:{settings.email}">
                            {settings.email}
                        </a>
                    </li>
                    <li style="align-items: start !important;">
                        <MapMarkerIcon class="mt-1" />
                        <a href="https://www.google.com/maps?q={settings.workshop_address_raw}" target="_blank">
                            <p><b>Delavnica:</b></p>
                            {@html settings.workshop_address}
                        </a>
                    </li>
                </ul>
            </div>
            <!-- 3. column - contact form -->
            <div class="footer-column">
                <div class="">
                    <h3>Pusti mi sporočilo</h3>
                </div>
                <form action="" class="flex flex-col gap-4 pt-2">
                    <!-- Name -->
                    <input type="text" class="input" placeholder="Ime" required>
                    <!-- Email -->
                    <input type="email" class="input" placeholder="Vaš email" required>
                    <!-- Message -->
                    <textarea name="" id="" rows="5" class="input resize-y" placeholder="Sporočilo" required></textarea>
                    <!-- Submit -->
                    <button type="submit" class="btn">POŠLJI</button>
                </form>
            </div>
        </div>
        
        <!-- Social & shoutout -->
        <div class="">
            <!-- Social -->
            <div class="py-5">
                <ul class="footer-social flex justify-center gap-4">
                    <li><a href={settings.instagram_url}><IGIcon /></a></li>
                    <li><a href={settings.facebook_url}><FacebookIcon /></a></li>
                    <li><a href="mailto:{settings.email}"><EmailIcon /></a></li>
                    <li><a href="tel:{settings.phone_number}"><PhoneIcon /></a></li>
                </ul>
            </div>
            
        </div>
    </div>

    <!-- Designed by me -->
    <div class="w-full bg-red-400 text-center">
        <a>Izdelal Vid</a>
    </div>
</footer>
