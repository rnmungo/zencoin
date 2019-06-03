<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- CSRF Token -->
        <meta name="csrf-token" content="{{ csrf_token() }}">

        <title>{{config('app.name', 'ZenCoin')}} - Iniciar Sesión</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Damion|Muli:400,600" rel="stylesheet" type="text/css">
        <!-- Scripts -->
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDu7tQ49-dLxuBPAb-Z3m3OfPCXRHB1RPQ" async defer></script>
        <script src="{{ asset('js/app.js') }}" defer></script>
        <script src="{{ asset('js/sweetalert.min.js') }}"></script>
        <!-- Styles -->
        <link rel="dns-prefetch" href="//fonts.gstatic.com">
        <link href="{{ asset('css/app.css') }}" rel="stylesheet">
        <link href="{{ asset('css/login.css') }}" rel="stylesheet">
    </head>
    <body>
        @include('sweet::alert')
        <div class="container" style="margin-top: 12%;">
            <div class="row justify-content-center mt-5 text-center">
                <div class="col-10 col-md-6 col-lg-4 shadow border bg-white">
                    <form id="login" method="POST" action="{{ route('login') }}" autocomplete="off">
                        @csrf
                        <img src="/imagenes/iconos/Flurry.png" class="img-fluid img-circle my-4" style="height: 6rem;" >
                        <div class="form-group row">
                            <div class="col-12">
                                <label class="field a-field a-field_a2 page__field">
                                    <input type="text" class="field__input a-field__input" placeholder=" " id="name" name="name" value="{{ old('name') }}" required>
                                    <span class="a-field__label-wrap">
                                        <span class="a-field__label">E-Mail</span>
                                    </span>
                                </label>
                            </div>
                        </div>
                        <div class="form-group row">
                            <div class="col-12">
                                <label class="field a-field a-field_a2 page__field">
                                    <input type="password" class="field__input a-field__input" placeholder=" " id="password" name="password" value="{{ old('password') }}" required>
                                    <span class="a-field__label-wrap">
                                        <span class="a-field__label">Contraseña</span>
                                    </span>
                                </label>
                            </div>
                        </div>
                        <div class="form-group row justify-content-center">
                            <div class="col-12">
                                <button type="button" class="btn btn-dark rounded shadow my-3">
                                    Iniciar Sesión
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </body>
</html>