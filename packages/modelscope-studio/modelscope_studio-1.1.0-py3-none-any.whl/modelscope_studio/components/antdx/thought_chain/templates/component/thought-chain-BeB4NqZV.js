import { i as er, a as ht, r as tr, g as nr, w as Ie, c as X } from "./Index-Uj0EUPVK.js";
const P = window.ms_globals.React, C = window.ms_globals.React, qn = window.ms_globals.React.isValidElement, Z = window.ms_globals.React.useRef, Qn = window.ms_globals.React.useLayoutEffect, pe = window.ms_globals.React.useEffect, Yn = window.ms_globals.React.forwardRef, Jn = window.ms_globals.React.useState, Zn = window.ms_globals.React.useMemo, At = window.ms_globals.ReactDOM, mt = window.ms_globals.ReactDOM.createPortal, rr = window.ms_globals.internalContext.useContextPropsContext, $t = window.ms_globals.internalContext.ContextPropsProvider, or = window.ms_globals.createItemsContext.createItemsContext, ir = window.ms_globals.antd.ConfigProvider, pt = window.ms_globals.antd.theme, sr = window.ms_globals.antd.Avatar, jt = window.ms_globals.antd.Typography, je = window.ms_globals.antdCssinjs.unit, et = window.ms_globals.antdCssinjs.token2CSSVar, zt = window.ms_globals.antdCssinjs.useStyleRegister, ar = window.ms_globals.antdCssinjs.useCSSVarRegister, cr = window.ms_globals.antdCssinjs.createTheme, lr = window.ms_globals.antdCssinjs.useCacheToken, ur = window.ms_globals.antdIcons.LeftOutlined, fr = window.ms_globals.antdIcons.RightOutlined;
var dr = /\s/;
function mr(e) {
  for (var t = e.length; t-- && dr.test(e.charAt(t)); )
    ;
  return t;
}
var hr = /^\s+/;
function pr(e) {
  return e && e.slice(0, mr(e) + 1).replace(hr, "");
}
var Dt = NaN, gr = /^[-+]0x[0-9a-f]+$/i, vr = /^0b[01]+$/i, yr = /^0o[0-7]+$/i, br = parseInt;
function kt(e) {
  if (typeof e == "number")
    return e;
  if (er(e))
    return Dt;
  if (ht(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = ht(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = pr(e);
  var r = vr.test(e);
  return r || yr.test(e) ? br(e.slice(2), r ? 2 : 8) : gr.test(e) ? Dt : +e;
}
var tt = function() {
  return tr.Date.now();
}, Sr = "Expected a function", xr = Math.max, Cr = Math.min;
function Er(e, t, r) {
  var o, n, i, s, a, c, l = 0, f = !1, u = !1, d = !0;
  if (typeof e != "function")
    throw new TypeError(Sr);
  t = kt(t) || 0, ht(r) && (f = !!r.leading, u = "maxWait" in r, i = u ? xr(kt(r.maxWait) || 0, t) : i, d = "trailing" in r ? !!r.trailing : d);
  function h(g) {
    var M = o, T = n;
    return o = n = void 0, l = g, s = e.apply(T, M), s;
  }
  function v(g) {
    return l = g, a = setTimeout(b, t), f ? h(g) : s;
  }
  function m(g) {
    var M = g - c, T = g - l, R = t - M;
    return u ? Cr(R, i - T) : R;
  }
  function p(g) {
    var M = g - c, T = g - l;
    return c === void 0 || M >= t || M < 0 || u && T >= i;
  }
  function b() {
    var g = tt();
    if (p(g))
      return S(g);
    a = setTimeout(b, m(g));
  }
  function S(g) {
    return a = void 0, d && o ? h(g) : (o = n = void 0, s);
  }
  function w() {
    a !== void 0 && clearTimeout(a), l = 0, o = c = n = a = void 0;
  }
  function y() {
    return a === void 0 ? s : S(tt());
  }
  function _() {
    var g = tt(), M = p(g);
    if (o = arguments, n = this, c = g, M) {
      if (a === void 0)
        return v(c);
      if (u)
        return clearTimeout(a), a = setTimeout(b, t), h(c);
    }
    return a === void 0 && (a = setTimeout(b, t)), s;
  }
  return _.cancel = w, _.flush = y, _;
}
var gn = {
  exports: {}
}, De = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var _r = C, wr = Symbol.for("react.element"), Tr = Symbol.for("react.fragment"), Mr = Object.prototype.hasOwnProperty, Pr = _r.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Or = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function vn(e, t, r) {
  var o, n = {}, i = null, s = null;
  r !== void 0 && (i = "" + r), t.key !== void 0 && (i = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (o in t) Mr.call(t, o) && !Or.hasOwnProperty(o) && (n[o] = t[o]);
  if (e && e.defaultProps) for (o in t = e.defaultProps, t) n[o] === void 0 && (n[o] = t[o]);
  return {
    $$typeof: wr,
    type: e,
    key: i,
    ref: s,
    props: n,
    _owner: Pr.current
  };
}
De.Fragment = Tr;
De.jsx = vn;
De.jsxs = vn;
gn.exports = De;
var ee = gn.exports;
const {
  SvelteComponent: Rr,
  assign: Ft,
  binding_callbacks: Ht,
  check_outros: Lr,
  children: yn,
  claim_element: bn,
  claim_space: Ir,
  component_subscribe: Nt,
  compute_slots: Ar,
  create_slot: $r,
  detach: ae,
  element: Sn,
  empty: Vt,
  exclude_internal_props: Bt,
  get_all_dirty_from_scope: jr,
  get_slot_changes: zr,
  group_outros: Dr,
  init: kr,
  insert_hydration: Ae,
  safe_not_equal: Fr,
  set_custom_element_data: xn,
  space: Hr,
  transition_in: $e,
  transition_out: gt,
  update_slot_base: Nr
} = window.__gradio__svelte__internal, {
  beforeUpdate: Vr,
  getContext: Br,
  onDestroy: Gr,
  setContext: Xr
} = window.__gradio__svelte__internal;
function Gt(e) {
  let t, r;
  const o = (
    /*#slots*/
    e[7].default
  ), n = $r(
    o,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Sn("svelte-slot"), n && n.c(), this.h();
    },
    l(i) {
      t = bn(i, "SVELTE-SLOT", {
        class: !0
      });
      var s = yn(t);
      n && n.l(s), s.forEach(ae), this.h();
    },
    h() {
      xn(t, "class", "svelte-1rt0kpf");
    },
    m(i, s) {
      Ae(i, t, s), n && n.m(t, null), e[9](t), r = !0;
    },
    p(i, s) {
      n && n.p && (!r || s & /*$$scope*/
      64) && Nr(
        n,
        o,
        i,
        /*$$scope*/
        i[6],
        r ? zr(
          o,
          /*$$scope*/
          i[6],
          s,
          null
        ) : jr(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      r || ($e(n, i), r = !0);
    },
    o(i) {
      gt(n, i), r = !1;
    },
    d(i) {
      i && ae(t), n && n.d(i), e[9](null);
    }
  };
}
function Ur(e) {
  let t, r, o, n, i = (
    /*$$slots*/
    e[4].default && Gt(e)
  );
  return {
    c() {
      t = Sn("react-portal-target"), r = Hr(), i && i.c(), o = Vt(), this.h();
    },
    l(s) {
      t = bn(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), yn(t).forEach(ae), r = Ir(s), i && i.l(s), o = Vt(), this.h();
    },
    h() {
      xn(t, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      Ae(s, t, a), e[8](t), Ae(s, r, a), i && i.m(s, a), Ae(s, o, a), n = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? i ? (i.p(s, a), a & /*$$slots*/
      16 && $e(i, 1)) : (i = Gt(s), i.c(), $e(i, 1), i.m(o.parentNode, o)) : i && (Dr(), gt(i, 1, 1, () => {
        i = null;
      }), Lr());
    },
    i(s) {
      n || ($e(i), n = !0);
    },
    o(s) {
      gt(i), n = !1;
    },
    d(s) {
      s && (ae(t), ae(r), ae(o)), e[8](null), i && i.d(s);
    }
  };
}
function Xt(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function Wr(e, t, r) {
  let o, n, {
    $$slots: i = {},
    $$scope: s
  } = t;
  const a = Ar(i);
  let {
    svelteInit: c
  } = t;
  const l = Ie(Xt(t)), f = Ie();
  Nt(e, f, (y) => r(0, o = y));
  const u = Ie();
  Nt(e, u, (y) => r(1, n = y));
  const d = [], h = Br("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: m,
    subSlotIndex: p
  } = nr() || {}, b = c({
    parent: h,
    props: l,
    target: f,
    slot: u,
    slotKey: v,
    slotIndex: m,
    subSlotIndex: p,
    onDestroy(y) {
      d.push(y);
    }
  });
  Xr("$$ms-gr-react-wrapper", b), Vr(() => {
    l.set(Xt(t));
  }), Gr(() => {
    d.forEach((y) => y());
  });
  function S(y) {
    Ht[y ? "unshift" : "push"](() => {
      o = y, f.set(o);
    });
  }
  function w(y) {
    Ht[y ? "unshift" : "push"](() => {
      n = y, u.set(n);
    });
  }
  return e.$$set = (y) => {
    r(17, t = Ft(Ft({}, t), Bt(y))), "svelteInit" in y && r(5, c = y.svelteInit), "$$scope" in y && r(6, s = y.$$scope);
  }, t = Bt(t), [o, n, f, u, a, c, s, i, S, w];
}
class Kr extends Rr {
  constructor(t) {
    super(), kr(this, t, Wr, Ur, Fr, {
      svelteInit: 5
    });
  }
}
const Ut = window.ms_globals.rerender, nt = window.ms_globals.tree;
function qr(e, t = {}) {
  function r(o) {
    const n = Ie(), i = new Kr({
      ...o,
      props: {
        svelteInit(s) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: n,
            reactComponent: e,
            props: s.props,
            slot: s.slot,
            target: s.target,
            slotIndex: s.slotIndex,
            subSlotIndex: s.subSlotIndex,
            ignore: t.ignore,
            slotKey: s.slotKey,
            nodes: []
          }, c = s.parent ?? nt;
          return c.nodes = [...c.nodes, a], Ut({
            createPortal: mt,
            node: nt
          }), s.onDestroy(() => {
            c.nodes = c.nodes.filter((l) => l.svelteInstance !== n), Ut({
              createPortal: mt,
              node: nt
            });
          }), a;
        },
        ...o.props
      }
    });
    return n.set(i), i;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(r);
    });
  });
}
const Qr = "1.0.5", Yr = /* @__PURE__ */ C.createContext({}), Jr = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, Zr = (e) => {
  const t = C.useContext(Yr);
  return C.useMemo(() => ({
    ...Jr,
    ...t[e]
  }), [t[e]]);
};
function ue() {
  return ue = Object.assign ? Object.assign.bind() : function(e) {
    for (var t = 1; t < arguments.length; t++) {
      var r = arguments[t];
      for (var o in r) ({}).hasOwnProperty.call(r, o) && (e[o] = r[o]);
    }
    return e;
  }, ue.apply(null, arguments);
}
const eo = "ant";
function vt() {
  const {
    getPrefixCls: e,
    direction: t,
    csp: r,
    iconPrefixCls: o,
    theme: n
  } = C.useContext(ir.ConfigContext);
  return {
    theme: n,
    getPrefixCls: e,
    direction: t,
    csp: r,
    iconPrefixCls: o
  };
}
function ge(e) {
  var t = P.useRef();
  t.current = e;
  var r = P.useCallback(function() {
    for (var o, n = arguments.length, i = new Array(n), s = 0; s < n; s++)
      i[s] = arguments[s];
    return (o = t.current) === null || o === void 0 ? void 0 : o.call.apply(o, [t].concat(i));
  }, []);
  return r;
}
function to(e) {
  if (Array.isArray(e)) return e;
}
function no(e, t) {
  var r = e == null ? null : typeof Symbol < "u" && e[Symbol.iterator] || e["@@iterator"];
  if (r != null) {
    var o, n, i, s, a = [], c = !0, l = !1;
    try {
      if (i = (r = r.call(e)).next, t === 0) {
        if (Object(r) !== r) return;
        c = !1;
      } else for (; !(c = (o = i.call(r)).done) && (a.push(o.value), a.length !== t); c = !0) ;
    } catch (f) {
      l = !0, n = f;
    } finally {
      try {
        if (!c && r.return != null && (s = r.return(), Object(s) !== s)) return;
      } finally {
        if (l) throw n;
      }
    }
    return a;
  }
}
function Wt(e, t) {
  (t == null || t > e.length) && (t = e.length);
  for (var r = 0, o = Array(t); r < t; r++) o[r] = e[r];
  return o;
}
function ro(e, t) {
  if (e) {
    if (typeof e == "string") return Wt(e, t);
    var r = {}.toString.call(e).slice(8, -1);
    return r === "Object" && e.constructor && (r = e.constructor.name), r === "Map" || r === "Set" ? Array.from(e) : r === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? Wt(e, t) : void 0;
  }
}
function oo() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function H(e, t) {
  return to(e) || no(e, t) || ro(e, t) || oo();
}
function ke() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var Kt = ke() ? P.useLayoutEffect : P.useEffect, io = function(t, r) {
  var o = P.useRef(!0);
  Kt(function() {
    return t(o.current);
  }, r), Kt(function() {
    return o.current = !1, function() {
      o.current = !0;
    };
  }, []);
}, qt = function(t, r) {
  io(function(o) {
    if (!o)
      return t();
  }, r);
};
function ve(e) {
  var t = P.useRef(!1), r = P.useState(e), o = H(r, 2), n = o[0], i = o[1];
  P.useEffect(function() {
    return t.current = !1, function() {
      t.current = !0;
    };
  }, []);
  function s(a, c) {
    c && t.current || i(a);
  }
  return [n, s];
}
function rt(e) {
  return e !== void 0;
}
function so(e, t) {
  var r = {}, o = r.defaultValue, n = r.value, i = r.onChange, s = r.postState, a = ve(function() {
    return rt(n) ? n : rt(o) ? typeof o == "function" ? o() : o : typeof e == "function" ? e() : e;
  }), c = H(a, 2), l = c[0], f = c[1], u = n !== void 0 ? n : l, d = s ? s(u) : u, h = ge(i), v = ve([u]), m = H(v, 2), p = m[0], b = m[1];
  qt(function() {
    var w = p[0];
    l !== w && h(l, w);
  }, [p]), qt(function() {
    rt(n) || f(n);
  }, [n]);
  var S = ge(function(w, y) {
    f(w, y), b([u], y);
  });
  return [d, S];
}
function k(e) {
  "@babel/helpers - typeof";
  return k = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(t) {
    return typeof t;
  } : function(t) {
    return t && typeof Symbol == "function" && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t;
  }, k(e);
}
var Cn = {
  exports: {}
}, O = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Tt = Symbol.for("react.element"), Mt = Symbol.for("react.portal"), Fe = Symbol.for("react.fragment"), He = Symbol.for("react.strict_mode"), Ne = Symbol.for("react.profiler"), Ve = Symbol.for("react.provider"), Be = Symbol.for("react.context"), ao = Symbol.for("react.server_context"), Ge = Symbol.for("react.forward_ref"), Xe = Symbol.for("react.suspense"), Ue = Symbol.for("react.suspense_list"), We = Symbol.for("react.memo"), Ke = Symbol.for("react.lazy"), co = Symbol.for("react.offscreen"), En;
En = Symbol.for("react.module.reference");
function U(e) {
  if (typeof e == "object" && e !== null) {
    var t = e.$$typeof;
    switch (t) {
      case Tt:
        switch (e = e.type, e) {
          case Fe:
          case Ne:
          case He:
          case Xe:
          case Ue:
            return e;
          default:
            switch (e = e && e.$$typeof, e) {
              case ao:
              case Be:
              case Ge:
              case Ke:
              case We:
              case Ve:
                return e;
              default:
                return t;
            }
        }
      case Mt:
        return t;
    }
  }
}
O.ContextConsumer = Be;
O.ContextProvider = Ve;
O.Element = Tt;
O.ForwardRef = Ge;
O.Fragment = Fe;
O.Lazy = Ke;
O.Memo = We;
O.Portal = Mt;
O.Profiler = Ne;
O.StrictMode = He;
O.Suspense = Xe;
O.SuspenseList = Ue;
O.isAsyncMode = function() {
  return !1;
};
O.isConcurrentMode = function() {
  return !1;
};
O.isContextConsumer = function(e) {
  return U(e) === Be;
};
O.isContextProvider = function(e) {
  return U(e) === Ve;
};
O.isElement = function(e) {
  return typeof e == "object" && e !== null && e.$$typeof === Tt;
};
O.isForwardRef = function(e) {
  return U(e) === Ge;
};
O.isFragment = function(e) {
  return U(e) === Fe;
};
O.isLazy = function(e) {
  return U(e) === Ke;
};
O.isMemo = function(e) {
  return U(e) === We;
};
O.isPortal = function(e) {
  return U(e) === Mt;
};
O.isProfiler = function(e) {
  return U(e) === Ne;
};
O.isStrictMode = function(e) {
  return U(e) === He;
};
O.isSuspense = function(e) {
  return U(e) === Xe;
};
O.isSuspenseList = function(e) {
  return U(e) === Ue;
};
O.isValidElementType = function(e) {
  return typeof e == "string" || typeof e == "function" || e === Fe || e === Ne || e === He || e === Xe || e === Ue || e === co || typeof e == "object" && e !== null && (e.$$typeof === Ke || e.$$typeof === We || e.$$typeof === Ve || e.$$typeof === Be || e.$$typeof === Ge || e.$$typeof === En || e.getModuleId !== void 0);
};
O.typeOf = U;
Cn.exports = O;
var ot = Cn.exports, lo = Symbol.for("react.element"), uo = Symbol.for("react.transitional.element"), fo = Symbol.for("react.fragment");
function mo(e) {
  return (
    // Base object type
    e && k(e) === "object" && // React Element type
    (e.$$typeof === lo || e.$$typeof === uo) && // React Fragment type
    e.type === fo
  );
}
var ho = function(t, r) {
  typeof t == "function" ? t(r) : k(t) === "object" && t && "current" in t && (t.current = r);
}, po = function(t) {
  var r, o;
  if (!t)
    return !1;
  if (_n(t) && t.props.propertyIsEnumerable("ref"))
    return !0;
  var n = ot.isMemo(t) ? t.type.type : t.type;
  return !(typeof n == "function" && !((r = n.prototype) !== null && r !== void 0 && r.render) && n.$$typeof !== ot.ForwardRef || typeof t == "function" && !((o = t.prototype) !== null && o !== void 0 && o.render) && t.$$typeof !== ot.ForwardRef);
};
function _n(e) {
  return /* @__PURE__ */ qn(e) && !mo(e);
}
var go = function(t) {
  if (t && _n(t)) {
    var r = t;
    return r.props.propertyIsEnumerable("ref") ? r.props.ref : r.ref;
  }
  return null;
};
function vo(e, t) {
  if (k(e) != "object" || !e) return e;
  var r = e[Symbol.toPrimitive];
  if (r !== void 0) {
    var o = r.call(e, t || "default");
    if (k(o) != "object") return o;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (t === "string" ? String : Number)(e);
}
function wn(e) {
  var t = vo(e, "string");
  return k(t) == "symbol" ? t : t + "";
}
function E(e, t, r) {
  return (t = wn(t)) in e ? Object.defineProperty(e, t, {
    value: r,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : e[t] = r, e;
}
function Qt(e, t) {
  var r = Object.keys(e);
  if (Object.getOwnPropertySymbols) {
    var o = Object.getOwnPropertySymbols(e);
    t && (o = o.filter(function(n) {
      return Object.getOwnPropertyDescriptor(e, n).enumerable;
    })), r.push.apply(r, o);
  }
  return r;
}
function x(e) {
  for (var t = 1; t < arguments.length; t++) {
    var r = arguments[t] != null ? arguments[t] : {};
    t % 2 ? Qt(Object(r), !0).forEach(function(o) {
      E(e, o, r[o]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Qt(Object(r)).forEach(function(o) {
      Object.defineProperty(e, o, Object.getOwnPropertyDescriptor(r, o));
    });
  }
  return e;
}
function Yt(e) {
  return e instanceof HTMLElement || e instanceof SVGElement;
}
function yo(e) {
  return e && k(e) === "object" && Yt(e.nativeElement) ? e.nativeElement : Yt(e) ? e : null;
}
function bo(e) {
  var t = yo(e);
  if (t)
    return t;
  if (e instanceof C.Component) {
    var r;
    return (r = At.findDOMNode) === null || r === void 0 ? void 0 : r.call(At, e);
  }
  return null;
}
function So(e, t) {
  if (e == null) return {};
  var r = {};
  for (var o in e) if ({}.hasOwnProperty.call(e, o)) {
    if (t.includes(o)) continue;
    r[o] = e[o];
  }
  return r;
}
function Jt(e, t) {
  if (e == null) return {};
  var r, o, n = So(e, t);
  if (Object.getOwnPropertySymbols) {
    var i = Object.getOwnPropertySymbols(e);
    for (o = 0; o < i.length; o++) r = i[o], t.includes(r) || {}.propertyIsEnumerable.call(e, r) && (n[r] = e[r]);
  }
  return n;
}
var xo = /* @__PURE__ */ P.createContext({});
function fe(e, t) {
  if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function Zt(e, t) {
  for (var r = 0; r < t.length; r++) {
    var o = t[r];
    o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(e, wn(o.key), o);
  }
}
function de(e, t, r) {
  return t && Zt(e.prototype, t), r && Zt(e, r), Object.defineProperty(e, "prototype", {
    writable: !1
  }), e;
}
function yt(e, t) {
  return yt = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(r, o) {
    return r.__proto__ = o, r;
  }, yt(e, t);
}
function qe(e, t) {
  if (typeof t != "function" && t !== null) throw new TypeError("Super expression must either be null or a function");
  e.prototype = Object.create(t && t.prototype, {
    constructor: {
      value: e,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(e, "prototype", {
    writable: !1
  }), t && yt(e, t);
}
function ze(e) {
  return ze = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
    return t.__proto__ || Object.getPrototypeOf(t);
  }, ze(e);
}
function Tn() {
  try {
    var e = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (Tn = function() {
    return !!e;
  })();
}
function se(e) {
  if (e === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return e;
}
function Co(e, t) {
  if (t && (k(t) == "object" || typeof t == "function")) return t;
  if (t !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return se(e);
}
function Qe(e) {
  var t = Tn();
  return function() {
    var r, o = ze(e);
    if (t) {
      var n = ze(this).constructor;
      r = Reflect.construct(o, arguments, n);
    } else r = o.apply(this, arguments);
    return Co(this, r);
  };
}
var Eo = /* @__PURE__ */ function(e) {
  qe(r, e);
  var t = Qe(r);
  function r() {
    return fe(this, r), t.apply(this, arguments);
  }
  return de(r, [{
    key: "render",
    value: function() {
      return this.props.children;
    }
  }]), r;
}(P.Component);
function _o(e) {
  var t = P.useReducer(function(a) {
    return a + 1;
  }, 0), r = H(t, 2), o = r[1], n = P.useRef(e), i = ge(function() {
    return n.current;
  }), s = ge(function(a) {
    n.current = typeof a == "function" ? a(n.current) : a, o();
  });
  return [i, s];
}
var J = "none", Me = "appear", Pe = "enter", Oe = "leave", en = "none", W = "prepare", ce = "start", le = "active", Pt = "end", Mn = "prepared";
function tn(e, t) {
  var r = {};
  return r[e.toLowerCase()] = t.toLowerCase(), r["Webkit".concat(e)] = "webkit".concat(t), r["Moz".concat(e)] = "moz".concat(t), r["ms".concat(e)] = "MS".concat(t), r["O".concat(e)] = "o".concat(t.toLowerCase()), r;
}
function wo(e, t) {
  var r = {
    animationend: tn("Animation", "AnimationEnd"),
    transitionend: tn("Transition", "TransitionEnd")
  };
  return e && ("AnimationEvent" in t || delete r.animationend.animation, "TransitionEvent" in t || delete r.transitionend.transition), r;
}
var To = wo(ke(), typeof window < "u" ? window : {}), Pn = {};
if (ke()) {
  var Mo = document.createElement("div");
  Pn = Mo.style;
}
var Re = {};
function On(e) {
  if (Re[e])
    return Re[e];
  var t = To[e];
  if (t)
    for (var r = Object.keys(t), o = r.length, n = 0; n < o; n += 1) {
      var i = r[n];
      if (Object.prototype.hasOwnProperty.call(t, i) && i in Pn)
        return Re[e] = t[i], Re[e];
    }
  return "";
}
var Rn = On("animationend"), Ln = On("transitionend"), In = !!(Rn && Ln), nn = Rn || "animationend", rn = Ln || "transitionend";
function on(e, t) {
  if (!e) return null;
  if (k(e) === "object") {
    var r = t.replace(/-\w/g, function(o) {
      return o[1].toUpperCase();
    });
    return e[r];
  }
  return "".concat(e, "-").concat(t);
}
const Po = function(e) {
  var t = Z();
  function r(n) {
    n && (n.removeEventListener(rn, e), n.removeEventListener(nn, e));
  }
  function o(n) {
    t.current && t.current !== n && r(t.current), n && n !== t.current && (n.addEventListener(rn, e), n.addEventListener(nn, e), t.current = n);
  }
  return P.useEffect(function() {
    return function() {
      r(t.current);
    };
  }, []), [o, r];
};
var An = ke() ? Qn : pe, $n = function(t) {
  return +setTimeout(t, 16);
}, jn = function(t) {
  return clearTimeout(t);
};
typeof window < "u" && "requestAnimationFrame" in window && ($n = function(t) {
  return window.requestAnimationFrame(t);
}, jn = function(t) {
  return window.cancelAnimationFrame(t);
});
var sn = 0, Ot = /* @__PURE__ */ new Map();
function zn(e) {
  Ot.delete(e);
}
var bt = function(t) {
  var r = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 1;
  sn += 1;
  var o = sn;
  function n(i) {
    if (i === 0)
      zn(o), t();
    else {
      var s = $n(function() {
        n(i - 1);
      });
      Ot.set(o, s);
    }
  }
  return n(r), o;
};
bt.cancel = function(e) {
  var t = Ot.get(e);
  return zn(e), jn(t);
};
const Oo = function() {
  var e = P.useRef(null);
  function t() {
    bt.cancel(e.current);
  }
  function r(o) {
    var n = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 2;
    t();
    var i = bt(function() {
      n <= 1 ? o({
        isCanceled: function() {
          return i !== e.current;
        }
      }) : r(o, n - 1);
    });
    e.current = i;
  }
  return P.useEffect(function() {
    return function() {
      t();
    };
  }, []), [r, t];
};
var Ro = [W, ce, le, Pt], Lo = [W, Mn], Dn = !1, Io = !0;
function kn(e) {
  return e === le || e === Pt;
}
const Ao = function(e, t, r) {
  var o = ve(en), n = H(o, 2), i = n[0], s = n[1], a = Oo(), c = H(a, 2), l = c[0], f = c[1];
  function u() {
    s(W, !0);
  }
  var d = t ? Lo : Ro;
  return An(function() {
    if (i !== en && i !== Pt) {
      var h = d.indexOf(i), v = d[h + 1], m = r(i);
      m === Dn ? s(v, !0) : v && l(function(p) {
        function b() {
          p.isCanceled() || s(v, !0);
        }
        m === !0 ? b() : Promise.resolve(m).then(b);
      });
    }
  }, [e, i]), P.useEffect(function() {
    return function() {
      f();
    };
  }, []), [u, i];
};
function $o(e, t, r, o) {
  var n = o.motionEnter, i = n === void 0 ? !0 : n, s = o.motionAppear, a = s === void 0 ? !0 : s, c = o.motionLeave, l = c === void 0 ? !0 : c, f = o.motionDeadline, u = o.motionLeaveImmediately, d = o.onAppearPrepare, h = o.onEnterPrepare, v = o.onLeavePrepare, m = o.onAppearStart, p = o.onEnterStart, b = o.onLeaveStart, S = o.onAppearActive, w = o.onEnterActive, y = o.onLeaveActive, _ = o.onAppearEnd, g = o.onEnterEnd, M = o.onLeaveEnd, T = o.onVisibleChanged, R = ve(), L = H(R, 2), I = L[0], A = L[1], $ = _o(J), j = H($, 2), z = j[0], V = j[1], te = ve(null), Y = H(te, 2), ye = Y[0], be = Y[1], B = z(), ne = Z(!1), me = Z(null);
  function G() {
    return r();
  }
  var re = Z(!1);
  function Se() {
    V(J), be(null, !0);
  }
  var q = ge(function(N) {
    var F = z();
    if (F !== J) {
      var K = G();
      if (!(N && !N.deadline && N.target !== K)) {
        var we = re.current, Te;
        F === Me && we ? Te = _ == null ? void 0 : _(K, N) : F === Pe && we ? Te = g == null ? void 0 : g(K, N) : F === Oe && we && (Te = M == null ? void 0 : M(K, N)), we && Te !== !1 && Se();
      }
    }
  }), Ye = Po(q), xe = H(Ye, 1), Ce = xe[0], Ee = function(F) {
    switch (F) {
      case Me:
        return E(E(E({}, W, d), ce, m), le, S);
      case Pe:
        return E(E(E({}, W, h), ce, p), le, w);
      case Oe:
        return E(E(E({}, W, v), ce, b), le, y);
      default:
        return {};
    }
  }, oe = P.useMemo(function() {
    return Ee(B);
  }, [B]), _e = Ao(B, !e, function(N) {
    if (N === W) {
      var F = oe[W];
      return F ? F(G()) : Dn;
    }
    if (ie in oe) {
      var K;
      be(((K = oe[ie]) === null || K === void 0 ? void 0 : K.call(oe, G(), null)) || null);
    }
    return ie === le && B !== J && (Ce(G()), f > 0 && (clearTimeout(me.current), me.current = setTimeout(function() {
      q({
        deadline: !0
      });
    }, f))), ie === Mn && Se(), Io;
  }), Lt = H(_e, 2), Wn = Lt[0], ie = Lt[1], Kn = kn(ie);
  re.current = Kn;
  var It = Z(null);
  An(function() {
    if (!(ne.current && It.current === t)) {
      A(t);
      var N = ne.current;
      ne.current = !0;
      var F;
      !N && t && a && (F = Me), N && t && i && (F = Pe), (N && !t && l || !N && u && !t && l) && (F = Oe);
      var K = Ee(F);
      F && (e || K[W]) ? (V(F), Wn()) : V(J), It.current = t;
    }
  }, [t]), pe(function() {
    // Cancel appear
    (B === Me && !a || // Cancel enter
    B === Pe && !i || // Cancel leave
    B === Oe && !l) && V(J);
  }, [a, i, l]), pe(function() {
    return function() {
      ne.current = !1, clearTimeout(me.current);
    };
  }, []);
  var Je = P.useRef(!1);
  pe(function() {
    I && (Je.current = !0), I !== void 0 && B === J && ((Je.current || I) && (T == null || T(I)), Je.current = !0);
  }, [I, B]);
  var Ze = ye;
  return oe[W] && ie === ce && (Ze = x({
    transition: "none"
  }, Ze)), [B, ie, Ze, I ?? t];
}
function jo(e) {
  var t = e;
  k(e) === "object" && (t = e.transitionSupport);
  function r(n, i) {
    return !!(n.motionName && t && i !== !1);
  }
  var o = /* @__PURE__ */ P.forwardRef(function(n, i) {
    var s = n.visible, a = s === void 0 ? !0 : s, c = n.removeOnLeave, l = c === void 0 ? !0 : c, f = n.forceRender, u = n.children, d = n.motionName, h = n.leavedClassName, v = n.eventProps, m = P.useContext(xo), p = m.motion, b = r(n, p), S = Z(), w = Z();
    function y() {
      try {
        return S.current instanceof HTMLElement ? S.current : bo(w.current);
      } catch {
        return null;
      }
    }
    var _ = $o(b, a, y, n), g = H(_, 4), M = g[0], T = g[1], R = g[2], L = g[3], I = P.useRef(L);
    L && (I.current = !0);
    var A = P.useCallback(function(Y) {
      S.current = Y, ho(i, Y);
    }, [i]), $, j = x(x({}, v), {}, {
      visible: a
    });
    if (!u)
      $ = null;
    else if (M === J)
      L ? $ = u(x({}, j), A) : !l && I.current && h ? $ = u(x(x({}, j), {}, {
        className: h
      }), A) : f || !l && !h ? $ = u(x(x({}, j), {}, {
        style: {
          display: "none"
        }
      }), A) : $ = null;
    else {
      var z;
      T === W ? z = "prepare" : kn(T) ? z = "active" : T === ce && (z = "start");
      var V = on(d, "".concat(M, "-").concat(z));
      $ = u(x(x({}, j), {}, {
        className: X(on(d, M), E(E({}, V, V && z), d, typeof d == "string")),
        style: R
      }), A);
    }
    if (/* @__PURE__ */ P.isValidElement($) && po($)) {
      var te = go($);
      te || ($ = /* @__PURE__ */ P.cloneElement($, {
        ref: A
      }));
    }
    return /* @__PURE__ */ P.createElement(Eo, {
      ref: w
    }, $);
  });
  return o.displayName = "CSSMotion", o;
}
const Fn = jo(In);
var St = "add", xt = "keep", Ct = "remove", it = "removed";
function zo(e) {
  var t;
  return e && k(e) === "object" && "key" in e ? t = e : t = {
    key: e
  }, x(x({}, t), {}, {
    key: String(t.key)
  });
}
function Et() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [];
  return e.map(zo);
}
function Do() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [], t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : [], r = [], o = 0, n = t.length, i = Et(e), s = Et(t);
  i.forEach(function(l) {
    for (var f = !1, u = o; u < n; u += 1) {
      var d = s[u];
      if (d.key === l.key) {
        o < u && (r = r.concat(s.slice(o, u).map(function(h) {
          return x(x({}, h), {}, {
            status: St
          });
        })), o = u), r.push(x(x({}, d), {}, {
          status: xt
        })), o += 1, f = !0;
        break;
      }
    }
    f || r.push(x(x({}, l), {}, {
      status: Ct
    }));
  }), o < n && (r = r.concat(s.slice(o).map(function(l) {
    return x(x({}, l), {}, {
      status: St
    });
  })));
  var a = {};
  r.forEach(function(l) {
    var f = l.key;
    a[f] = (a[f] || 0) + 1;
  });
  var c = Object.keys(a).filter(function(l) {
    return a[l] > 1;
  });
  return c.forEach(function(l) {
    r = r.filter(function(f) {
      var u = f.key, d = f.status;
      return u !== l || d !== Ct;
    }), r.forEach(function(f) {
      f.key === l && (f.status = xt);
    });
  }), r;
}
var ko = ["component", "children", "onVisibleChanged", "onAllRemoved"], Fo = ["status"], Ho = ["eventProps", "visible", "children", "motionName", "motionAppear", "motionEnter", "motionLeave", "motionLeaveImmediately", "motionDeadline", "removeOnLeave", "leavedClassName", "onAppearPrepare", "onAppearStart", "onAppearActive", "onAppearEnd", "onEnterStart", "onEnterActive", "onEnterEnd", "onLeaveStart", "onLeaveActive", "onLeaveEnd"];
function No(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : Fn, r = /* @__PURE__ */ function(o) {
    qe(i, o);
    var n = Qe(i);
    function i() {
      var s;
      fe(this, i);
      for (var a = arguments.length, c = new Array(a), l = 0; l < a; l++)
        c[l] = arguments[l];
      return s = n.call.apply(n, [this].concat(c)), E(se(s), "state", {
        keyEntities: []
      }), E(se(s), "removeKey", function(f) {
        s.setState(function(u) {
          var d = u.keyEntities.map(function(h) {
            return h.key !== f ? h : x(x({}, h), {}, {
              status: it
            });
          });
          return {
            keyEntities: d
          };
        }, function() {
          var u = s.state.keyEntities, d = u.filter(function(h) {
            var v = h.status;
            return v !== it;
          }).length;
          d === 0 && s.props.onAllRemoved && s.props.onAllRemoved();
        });
      }), s;
    }
    return de(i, [{
      key: "render",
      value: function() {
        var a = this, c = this.state.keyEntities, l = this.props, f = l.component, u = l.children, d = l.onVisibleChanged;
        l.onAllRemoved;
        var h = Jt(l, ko), v = f || P.Fragment, m = {};
        return Ho.forEach(function(p) {
          m[p] = h[p], delete h[p];
        }), delete h.keys, /* @__PURE__ */ P.createElement(v, h, c.map(function(p, b) {
          var S = p.status, w = Jt(p, Fo), y = S === St || S === xt;
          return /* @__PURE__ */ P.createElement(t, ue({}, m, {
            key: w.key,
            visible: y,
            eventProps: w,
            onVisibleChanged: function(g) {
              d == null || d(g, {
                key: w.key
              }), g || a.removeKey(w.key);
            }
          }), function(_, g) {
            return u(x(x({}, _), {}, {
              index: b
            }), g);
          });
        }));
      }
    }], [{
      key: "getDerivedStateFromProps",
      value: function(a, c) {
        var l = a.keys, f = c.keyEntities, u = Et(l), d = Do(f, u);
        return {
          keyEntities: d.filter(function(h) {
            var v = f.find(function(m) {
              var p = m.key;
              return h.key === p;
            });
            return !(v && v.status === it && h.status === Ct);
          })
        };
      }
    }]), i;
  }(P.Component);
  return E(r, "defaultProps", {
    component: "div"
  }), r;
}
No(In);
var Hn = /* @__PURE__ */ de(function e() {
  fe(this, e);
}), Nn = "CALC_UNIT", Vo = new RegExp(Nn, "g");
function st(e) {
  return typeof e == "number" ? "".concat(e).concat(Nn) : e;
}
var Bo = /* @__PURE__ */ function(e) {
  qe(r, e);
  var t = Qe(r);
  function r(o, n) {
    var i;
    fe(this, r), i = t.call(this), E(se(i), "result", ""), E(se(i), "unitlessCssVar", void 0), E(se(i), "lowPriority", void 0);
    var s = k(o);
    return i.unitlessCssVar = n, o instanceof r ? i.result = "(".concat(o.result, ")") : s === "number" ? i.result = st(o) : s === "string" && (i.result = o), i;
  }
  return de(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " + ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " + ").concat(st(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " - ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " - ").concat(st(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " * ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " * ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " / ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " / ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(n) {
      return this.lowPriority || n ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(n) {
      var i = this, s = n || {}, a = s.unit, c = !0;
      return typeof a == "boolean" ? c = a : Array.from(this.unitlessCssVar).some(function(l) {
        return i.result.includes(l);
      }) && (c = !1), this.result = this.result.replace(Vo, c ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), r;
}(Hn), Go = /* @__PURE__ */ function(e) {
  qe(r, e);
  var t = Qe(r);
  function r(o) {
    var n;
    return fe(this, r), n = t.call(this), E(se(n), "result", 0), o instanceof r ? n.result = o.result : typeof o == "number" && (n.result = o), n;
  }
  return de(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result += n.result : typeof n == "number" && (this.result += n), this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result -= n.result : typeof n == "number" && (this.result -= n), this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return n instanceof r ? this.result *= n.result : typeof n == "number" && (this.result *= n), this;
    }
  }, {
    key: "div",
    value: function(n) {
      return n instanceof r ? this.result /= n.result : typeof n == "number" && (this.result /= n), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), r;
}(Hn), Xo = function(t, r) {
  var o = t === "css" ? Bo : Go;
  return function(n) {
    return new o(n, r);
  };
}, an = function(t, r) {
  return "".concat([r, t.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function cn(e, t, r, o) {
  var n = x({}, t[e]);
  if (o != null && o.deprecatedTokens) {
    var i = o.deprecatedTokens;
    i.forEach(function(a) {
      var c = H(a, 2), l = c[0], f = c[1];
      if (n != null && n[l] || n != null && n[f]) {
        var u;
        (u = n[f]) !== null && u !== void 0 || (n[f] = n == null ? void 0 : n[l]);
      }
    });
  }
  var s = x(x({}, r), n);
  return Object.keys(s).forEach(function(a) {
    s[a] === t[a] && delete s[a];
  }), s;
}
var Vn = typeof CSSINJS_STATISTIC < "u", _t = !0;
function Rt() {
  for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
    t[r] = arguments[r];
  if (!Vn)
    return Object.assign.apply(Object, [{}].concat(t));
  _t = !1;
  var o = {};
  return t.forEach(function(n) {
    if (k(n) === "object") {
      var i = Object.keys(n);
      i.forEach(function(s) {
        Object.defineProperty(o, s, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return n[s];
          }
        });
      });
    }
  }), _t = !0, o;
}
var ln = {};
function Uo() {
}
var Wo = function(t) {
  var r, o = t, n = Uo;
  return Vn && typeof Proxy < "u" && (r = /* @__PURE__ */ new Set(), o = new Proxy(t, {
    get: function(s, a) {
      if (_t) {
        var c;
        (c = r) === null || c === void 0 || c.add(a);
      }
      return s[a];
    }
  }), n = function(s, a) {
    var c;
    ln[s] = {
      global: Array.from(r),
      component: x(x({}, (c = ln[s]) === null || c === void 0 ? void 0 : c.component), a)
    };
  }), {
    token: o,
    keys: r,
    flush: n
  };
};
function un(e, t, r) {
  if (typeof r == "function") {
    var o;
    return r(Rt(t, (o = t[e]) !== null && o !== void 0 ? o : {}));
  }
  return r ?? {};
}
function Ko(e) {
  return e === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "max(".concat(o.map(function(i) {
        return je(i);
      }).join(","), ")");
    },
    min: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "min(".concat(o.map(function(i) {
        return je(i);
      }).join(","), ")");
    }
  };
}
var qo = 1e3 * 60 * 10, Qo = /* @__PURE__ */ function() {
  function e() {
    fe(this, e), E(this, "map", /* @__PURE__ */ new Map()), E(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), E(this, "nextID", 0), E(this, "lastAccessBeat", /* @__PURE__ */ new Map()), E(this, "accessBeat", 0);
  }
  return de(e, [{
    key: "set",
    value: function(r, o) {
      this.clear();
      var n = this.getCompositeKey(r);
      this.map.set(n, o), this.lastAccessBeat.set(n, Date.now());
    }
  }, {
    key: "get",
    value: function(r) {
      var o = this.getCompositeKey(r), n = this.map.get(o);
      return this.lastAccessBeat.set(o, Date.now()), this.accessBeat += 1, n;
    }
  }, {
    key: "getCompositeKey",
    value: function(r) {
      var o = this, n = r.map(function(i) {
        return i && k(i) === "object" ? "obj_".concat(o.getObjectID(i)) : "".concat(k(i), "_").concat(i);
      });
      return n.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(r) {
      if (this.objectIDMap.has(r))
        return this.objectIDMap.get(r);
      var o = this.nextID;
      return this.objectIDMap.set(r, o), this.nextID += 1, o;
    }
  }, {
    key: "clear",
    value: function() {
      var r = this;
      if (this.accessBeat > 1e4) {
        var o = Date.now();
        this.lastAccessBeat.forEach(function(n, i) {
          o - n > qo && (r.map.delete(i), r.lastAccessBeat.delete(i));
        }), this.accessBeat = 0;
      }
    }
  }]), e;
}(), fn = new Qo();
function Yo(e, t) {
  return C.useMemo(function() {
    var r = fn.get(t);
    if (r)
      return r;
    var o = e();
    return fn.set(t, o), o;
  }, t);
}
var Jo = function() {
  return {};
};
function Zo(e) {
  var t = e.useCSP, r = t === void 0 ? Jo : t, o = e.useToken, n = e.usePrefix, i = e.getResetStyles, s = e.getCommonStyle, a = e.getCompUnitless;
  function c(d, h, v, m) {
    var p = Array.isArray(d) ? d[0] : d;
    function b(T) {
      return "".concat(String(p)).concat(T.slice(0, 1).toUpperCase()).concat(T.slice(1));
    }
    var S = (m == null ? void 0 : m.unitless) || {}, w = typeof a == "function" ? a(d) : {}, y = x(x({}, w), {}, E({}, b("zIndexPopup"), !0));
    Object.keys(S).forEach(function(T) {
      y[b(T)] = S[T];
    });
    var _ = x(x({}, m), {}, {
      unitless: y,
      prefixToken: b
    }), g = f(d, h, v, _), M = l(p, v, _);
    return function(T) {
      var R = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : T, L = g(T, R), I = H(L, 2), A = I[1], $ = M(R), j = H($, 2), z = j[0], V = j[1];
      return [z, A, V];
    };
  }
  function l(d, h, v) {
    var m = v.unitless, p = v.injectStyle, b = p === void 0 ? !0 : p, S = v.prefixToken, w = v.ignore, y = function(M) {
      var T = M.rootCls, R = M.cssVar, L = R === void 0 ? {} : R, I = o(), A = I.realToken;
      return ar({
        path: [d],
        prefix: L.prefix,
        key: L.key,
        unitless: m,
        ignore: w,
        token: A,
        scope: T
      }, function() {
        var $ = un(d, A, h), j = cn(d, A, $, {
          deprecatedTokens: v == null ? void 0 : v.deprecatedTokens
        });
        return Object.keys($).forEach(function(z) {
          j[S(z)] = j[z], delete j[z];
        }), j;
      }), null;
    }, _ = function(M) {
      var T = o(), R = T.cssVar;
      return [function(L) {
        return b && R ? /* @__PURE__ */ C.createElement(C.Fragment, null, /* @__PURE__ */ C.createElement(y, {
          rootCls: M,
          cssVar: R,
          component: d
        }), L) : L;
      }, R == null ? void 0 : R.key];
    };
    return _;
  }
  function f(d, h, v) {
    var m = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, p = Array.isArray(d) ? d : [d, d], b = H(p, 1), S = b[0], w = p.join("-"), y = e.layer || {
      name: "antd"
    };
    return function(_) {
      var g = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : _, M = o(), T = M.theme, R = M.realToken, L = M.hashId, I = M.token, A = M.cssVar, $ = n(), j = $.rootPrefixCls, z = $.iconPrefixCls, V = r(), te = A ? "css" : "js", Y = Yo(function() {
        var G = /* @__PURE__ */ new Set();
        return A && Object.keys(m.unitless || {}).forEach(function(re) {
          G.add(et(re, A.prefix)), G.add(et(re, an(S, A.prefix)));
        }), Xo(te, G);
      }, [te, S, A == null ? void 0 : A.prefix]), ye = Ko(te), be = ye.max, B = ye.min, ne = {
        theme: T,
        token: I,
        hashId: L,
        nonce: function() {
          return V.nonce;
        },
        clientOnly: m.clientOnly,
        layer: y,
        // antd is always at top of styles
        order: m.order || -999
      };
      typeof i == "function" && zt(x(x({}, ne), {}, {
        clientOnly: !1,
        path: ["Shared", j]
      }), function() {
        return i(I, {
          prefix: {
            rootPrefixCls: j,
            iconPrefixCls: z
          },
          csp: V
        });
      });
      var me = zt(x(x({}, ne), {}, {
        path: [w, _, z]
      }), function() {
        if (m.injectStyle === !1)
          return [];
        var G = Wo(I), re = G.token, Se = G.flush, q = un(S, R, v), Ye = ".".concat(_), xe = cn(S, R, q, {
          deprecatedTokens: m.deprecatedTokens
        });
        A && q && k(q) === "object" && Object.keys(q).forEach(function(_e) {
          q[_e] = "var(".concat(et(_e, an(S, A.prefix)), ")");
        });
        var Ce = Rt(re, {
          componentCls: Ye,
          prefixCls: _,
          iconCls: ".".concat(z),
          antCls: ".".concat(j),
          calc: Y,
          // @ts-ignore
          max: be,
          // @ts-ignore
          min: B
        }, A ? q : xe), Ee = h(Ce, {
          hashId: L,
          prefixCls: _,
          rootPrefixCls: j,
          iconPrefixCls: z
        });
        Se(S, xe);
        var oe = typeof s == "function" ? s(Ce, _, g, m.resetFont) : null;
        return [m.resetStyle === !1 ? null : oe, Ee];
      });
      return [me, L];
    };
  }
  function u(d, h, v) {
    var m = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, p = f(d, h, v, x({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, m)), b = function(w) {
      var y = w.prefixCls, _ = w.rootCls, g = _ === void 0 ? y : _;
      return p(y, g), null;
    };
    return b;
  }
  return {
    genStyleHooks: c,
    genSubStyleComponent: u,
    genComponentStyleHook: f
  };
}
const D = Math.round;
function at(e, t) {
  const r = e.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], o = r.map((n) => parseFloat(n));
  for (let n = 0; n < 3; n += 1)
    o[n] = t(o[n] || 0, r[n] || "", n);
  return r[3] ? o[3] = r[3].includes("%") ? o[3] / 100 : o[3] : o[3] = 1, o;
}
const dn = (e, t, r) => r === 0 ? e : e / 100;
function he(e, t) {
  const r = t || 255;
  return e > r ? r : e < 0 ? 0 : e;
}
class Q {
  constructor(t) {
    E(this, "isValid", !0), E(this, "r", 0), E(this, "g", 0), E(this, "b", 0), E(this, "a", 1), E(this, "_h", void 0), E(this, "_s", void 0), E(this, "_l", void 0), E(this, "_v", void 0), E(this, "_max", void 0), E(this, "_min", void 0), E(this, "_brightness", void 0);
    function r(o) {
      return o[0] in t && o[1] in t && o[2] in t;
    }
    if (t) if (typeof t == "string") {
      let n = function(i) {
        return o.startsWith(i);
      };
      const o = t.trim();
      /^#?[A-F\d]{3,8}$/i.test(o) ? this.fromHexString(o) : n("rgb") ? this.fromRgbString(o) : n("hsl") ? this.fromHslString(o) : (n("hsv") || n("hsb")) && this.fromHsvString(o);
    } else if (t instanceof Q)
      this.r = t.r, this.g = t.g, this.b = t.b, this.a = t.a, this._h = t._h, this._s = t._s, this._l = t._l, this._v = t._v;
    else if (r("rgb"))
      this.r = he(t.r), this.g = he(t.g), this.b = he(t.b), this.a = typeof t.a == "number" ? he(t.a, 1) : 1;
    else if (r("hsl"))
      this.fromHsl(t);
    else if (r("hsv"))
      this.fromHsv(t);
    else
      throw new Error("@ant-design/fast-color: unsupported input " + JSON.stringify(t));
  }
  // ======================= Setter =======================
  setR(t) {
    return this._sc("r", t);
  }
  setG(t) {
    return this._sc("g", t);
  }
  setB(t) {
    return this._sc("b", t);
  }
  setA(t) {
    return this._sc("a", t, 1);
  }
  setHue(t) {
    const r = this.toHsv();
    return r.h = t, this._c(r);
  }
  // ======================= Getter =======================
  /**
   * Returns the perceived luminance of a color, from 0-1.
   * @see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
   */
  getLuminance() {
    function t(i) {
      const s = i / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    }
    const r = t(this.r), o = t(this.g), n = t(this.b);
    return 0.2126 * r + 0.7152 * o + 0.0722 * n;
  }
  getHue() {
    if (typeof this._h > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._h = 0 : this._h = D(60 * (this.r === this.getMax() ? (this.g - this.b) / t + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / t + 2 : (this.r - this.g) / t + 4));
    }
    return this._h;
  }
  getSaturation() {
    if (typeof this._s > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._s = 0 : this._s = t / this.getMax();
    }
    return this._s;
  }
  getLightness() {
    return typeof this._l > "u" && (this._l = (this.getMax() + this.getMin()) / 510), this._l;
  }
  getValue() {
    return typeof this._v > "u" && (this._v = this.getMax() / 255), this._v;
  }
  /**
   * Returns the perceived brightness of the color, from 0-255.
   * Note: this is not the b of HSB
   * @see http://www.w3.org/TR/AERT#color-contrast
   */
  getBrightness() {
    return typeof this._brightness > "u" && (this._brightness = (this.r * 299 + this.g * 587 + this.b * 114) / 1e3), this._brightness;
  }
  // ======================== Func ========================
  darken(t = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() - t / 100;
    return n < 0 && (n = 0), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  lighten(t = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() + t / 100;
    return n > 1 && (n = 1), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(t, r = 50) {
    const o = this._c(t), n = r / 100, i = (a) => (o[a] - this[a]) * n + this[a], s = {
      r: D(i("r")),
      g: D(i("g")),
      b: D(i("b")),
      a: D(i("a") * 100) / 100
    };
    return this._c(s);
  }
  /**
   * Mix the color with pure white, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return white.
   */
  tint(t = 10) {
    return this.mix({
      r: 255,
      g: 255,
      b: 255,
      a: 1
    }, t);
  }
  /**
   * Mix the color with pure black, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return black.
   */
  shade(t = 10) {
    return this.mix({
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }, t);
  }
  onBackground(t) {
    const r = this._c(t), o = this.a + r.a * (1 - this.a), n = (i) => D((this[i] * this.a + r[i] * r.a * (1 - this.a)) / o);
    return this._c({
      r: n("r"),
      g: n("g"),
      b: n("b"),
      a: o
    });
  }
  // ======================= Status =======================
  isDark() {
    return this.getBrightness() < 128;
  }
  isLight() {
    return this.getBrightness() >= 128;
  }
  // ======================== MISC ========================
  equals(t) {
    return this.r === t.r && this.g === t.g && this.b === t.b && this.a === t.a;
  }
  clone() {
    return this._c(this);
  }
  // ======================= Format =======================
  toHexString() {
    let t = "#";
    const r = (this.r || 0).toString(16);
    t += r.length === 2 ? r : "0" + r;
    const o = (this.g || 0).toString(16);
    t += o.length === 2 ? o : "0" + o;
    const n = (this.b || 0).toString(16);
    if (t += n.length === 2 ? n : "0" + n, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const i = D(this.a * 255).toString(16);
      t += i.length === 2 ? i : "0" + i;
    }
    return t;
  }
  /** CSS support color pattern */
  toHsl() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      l: this.getLightness(),
      a: this.a
    };
  }
  /** CSS support color pattern */
  toHslString() {
    const t = this.getHue(), r = D(this.getSaturation() * 100), o = D(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${t},${r}%,${o}%,${this.a})` : `hsl(${t},${r}%,${o}%)`;
  }
  /** Same as toHsb */
  toHsv() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      v: this.getValue(),
      a: this.a
    };
  }
  toRgb() {
    return {
      r: this.r,
      g: this.g,
      b: this.b,
      a: this.a
    };
  }
  toRgbString() {
    return this.a !== 1 ? `rgba(${this.r},${this.g},${this.b},${this.a})` : `rgb(${this.r},${this.g},${this.b})`;
  }
  toString() {
    return this.toRgbString();
  }
  // ====================== Privates ======================
  /** Return a new FastColor object with one channel changed */
  _sc(t, r, o) {
    const n = this.clone();
    return n[t] = he(r, o), n;
  }
  _c(t) {
    return new this.constructor(t);
  }
  getMax() {
    return typeof this._max > "u" && (this._max = Math.max(this.r, this.g, this.b)), this._max;
  }
  getMin() {
    return typeof this._min > "u" && (this._min = Math.min(this.r, this.g, this.b)), this._min;
  }
  fromHexString(t) {
    const r = t.replace("#", "");
    function o(n, i) {
      return parseInt(r[n] + r[i || n], 16);
    }
    r.length < 6 ? (this.r = o(0), this.g = o(1), this.b = o(2), this.a = r[3] ? o(3) / 255 : 1) : (this.r = o(0, 1), this.g = o(2, 3), this.b = o(4, 5), this.a = r[6] ? o(6, 7) / 255 : 1);
  }
  fromHsl({
    h: t,
    s: r,
    l: o,
    a: n
  }) {
    if (this._h = t % 360, this._s = r, this._l = o, this.a = typeof n == "number" ? n : 1, r <= 0) {
      const d = D(o * 255);
      this.r = d, this.g = d, this.b = d;
    }
    let i = 0, s = 0, a = 0;
    const c = t / 60, l = (1 - Math.abs(2 * o - 1)) * r, f = l * (1 - Math.abs(c % 2 - 1));
    c >= 0 && c < 1 ? (i = l, s = f) : c >= 1 && c < 2 ? (i = f, s = l) : c >= 2 && c < 3 ? (s = l, a = f) : c >= 3 && c < 4 ? (s = f, a = l) : c >= 4 && c < 5 ? (i = f, a = l) : c >= 5 && c < 6 && (i = l, a = f);
    const u = o - l / 2;
    this.r = D((i + u) * 255), this.g = D((s + u) * 255), this.b = D((a + u) * 255);
  }
  fromHsv({
    h: t,
    s: r,
    v: o,
    a: n
  }) {
    this._h = t % 360, this._s = r, this._v = o, this.a = typeof n == "number" ? n : 1;
    const i = D(o * 255);
    if (this.r = i, this.g = i, this.b = i, r <= 0)
      return;
    const s = t / 60, a = Math.floor(s), c = s - a, l = D(o * (1 - r) * 255), f = D(o * (1 - r * c) * 255), u = D(o * (1 - r * (1 - c)) * 255);
    switch (a) {
      case 0:
        this.g = u, this.b = l;
        break;
      case 1:
        this.r = f, this.b = l;
        break;
      case 2:
        this.r = l, this.b = u;
        break;
      case 3:
        this.r = l, this.g = f;
        break;
      case 4:
        this.r = u, this.g = l;
        break;
      case 5:
      default:
        this.g = l, this.b = f;
        break;
    }
  }
  fromHsvString(t) {
    const r = at(t, dn);
    this.fromHsv({
      h: r[0],
      s: r[1],
      v: r[2],
      a: r[3]
    });
  }
  fromHslString(t) {
    const r = at(t, dn);
    this.fromHsl({
      h: r[0],
      s: r[1],
      l: r[2],
      a: r[3]
    });
  }
  fromRgbString(t) {
    const r = at(t, (o, n) => (
      // Convert percentage to number. e.g. 50% -> 128
      n.includes("%") ? D(o / 100 * 255) : o
    ));
    this.r = r[0], this.g = r[1], this.b = r[2], this.a = r[3];
  }
}
const ei = {
  blue: "#1677FF",
  purple: "#722ED1",
  cyan: "#13C2C2",
  green: "#52C41A",
  magenta: "#EB2F96",
  /**
   * @deprecated Use magenta instead
   */
  pink: "#EB2F96",
  red: "#F5222D",
  orange: "#FA8C16",
  yellow: "#FADB14",
  volcano: "#FA541C",
  geekblue: "#2F54EB",
  gold: "#FAAD14",
  lime: "#A0D911"
}, ti = Object.assign(Object.assign({}, ei), {
  // Color
  colorPrimary: "#1677ff",
  colorSuccess: "#52c41a",
  colorWarning: "#faad14",
  colorError: "#ff4d4f",
  colorInfo: "#1677ff",
  colorLink: "",
  colorTextBase: "",
  colorBgBase: "",
  // Font
  fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial,
'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
'Noto Color Emoji'`,
  fontFamilyCode: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace",
  fontSize: 14,
  // Line
  lineWidth: 1,
  lineType: "solid",
  // Motion
  motionUnit: 0.1,
  motionBase: 0,
  motionEaseOutCirc: "cubic-bezier(0.08, 0.82, 0.17, 1)",
  motionEaseInOutCirc: "cubic-bezier(0.78, 0.14, 0.15, 0.86)",
  motionEaseOut: "cubic-bezier(0.215, 0.61, 0.355, 1)",
  motionEaseInOut: "cubic-bezier(0.645, 0.045, 0.355, 1)",
  motionEaseOutBack: "cubic-bezier(0.12, 0.4, 0.29, 1.46)",
  motionEaseInBack: "cubic-bezier(0.71, -0.46, 0.88, 0.6)",
  motionEaseInQuint: "cubic-bezier(0.755, 0.05, 0.855, 0.06)",
  motionEaseOutQuint: "cubic-bezier(0.23, 1, 0.32, 1)",
  // Radius
  borderRadius: 6,
  // Size
  sizeUnit: 4,
  sizeStep: 4,
  sizePopupArrow: 16,
  // Control Base
  controlHeight: 32,
  // zIndex
  zIndexBase: 0,
  zIndexPopupBase: 1e3,
  // Image
  opacityImage: 1,
  // Wireframe
  wireframe: !1,
  // Motion
  motion: !0
});
function ct(e) {
  return e >= 0 && e <= 255;
}
function Le(e, t) {
  const {
    r,
    g: o,
    b: n,
    a: i
  } = new Q(e).toRgb();
  if (i < 1)
    return e;
  const {
    r: s,
    g: a,
    b: c
  } = new Q(t).toRgb();
  for (let l = 0.01; l <= 1; l += 0.01) {
    const f = Math.round((r - s * (1 - l)) / l), u = Math.round((o - a * (1 - l)) / l), d = Math.round((n - c * (1 - l)) / l);
    if (ct(f) && ct(u) && ct(d))
      return new Q({
        r: f,
        g: u,
        b: d,
        a: Math.round(l * 100) / 100
      }).toRgbString();
  }
  return new Q({
    r,
    g: o,
    b: n,
    a: 1
  }).toRgbString();
}
var ni = function(e, t) {
  var r = {};
  for (var o in e) Object.prototype.hasOwnProperty.call(e, o) && t.indexOf(o) < 0 && (r[o] = e[o]);
  if (e != null && typeof Object.getOwnPropertySymbols == "function") for (var n = 0, o = Object.getOwnPropertySymbols(e); n < o.length; n++)
    t.indexOf(o[n]) < 0 && Object.prototype.propertyIsEnumerable.call(e, o[n]) && (r[o[n]] = e[o[n]]);
  return r;
};
function ri(e) {
  const {
    override: t
  } = e, r = ni(e, ["override"]), o = Object.assign({}, t);
  Object.keys(ti).forEach((d) => {
    delete o[d];
  });
  const n = Object.assign(Object.assign({}, r), o), i = 480, s = 576, a = 768, c = 992, l = 1200, f = 1600;
  if (n.motion === !1) {
    const d = "0s";
    n.motionDurationFast = d, n.motionDurationMid = d, n.motionDurationSlow = d;
  }
  return Object.assign(Object.assign(Object.assign({}, n), {
    // ============== Background ============== //
    colorFillContent: n.colorFillSecondary,
    colorFillContentHover: n.colorFill,
    colorFillAlter: n.colorFillQuaternary,
    colorBgContainerDisabled: n.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: n.colorBgContainer,
    colorSplit: Le(n.colorBorderSecondary, n.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: n.colorTextQuaternary,
    colorTextDisabled: n.colorTextQuaternary,
    colorTextHeading: n.colorText,
    colorTextLabel: n.colorTextSecondary,
    colorTextDescription: n.colorTextTertiary,
    colorTextLightSolid: n.colorWhite,
    colorHighlight: n.colorError,
    colorBgTextHover: n.colorFillSecondary,
    colorBgTextActive: n.colorFill,
    colorIcon: n.colorTextTertiary,
    colorIconHover: n.colorText,
    colorErrorOutline: Le(n.colorErrorBg, n.colorBgContainer),
    colorWarningOutline: Le(n.colorWarningBg, n.colorBgContainer),
    // Font
    fontSizeIcon: n.fontSizeSM,
    // Line
    lineWidthFocus: n.lineWidth * 3,
    // Control
    lineWidth: n.lineWidth,
    controlOutlineWidth: n.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: n.controlHeight / 2,
    controlItemBgHover: n.colorFillTertiary,
    controlItemBgActive: n.colorPrimaryBg,
    controlItemBgActiveHover: n.colorPrimaryBgHover,
    controlItemBgActiveDisabled: n.colorFill,
    controlTmpOutline: n.colorFillQuaternary,
    controlOutline: Le(n.colorPrimaryBg, n.colorBgContainer),
    lineType: n.lineType,
    borderRadius: n.borderRadius,
    borderRadiusXS: n.borderRadiusXS,
    borderRadiusSM: n.borderRadiusSM,
    borderRadiusLG: n.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: n.sizeXXS,
    paddingXS: n.sizeXS,
    paddingSM: n.sizeSM,
    padding: n.size,
    paddingMD: n.sizeMD,
    paddingLG: n.sizeLG,
    paddingXL: n.sizeXL,
    paddingContentHorizontalLG: n.sizeLG,
    paddingContentVerticalLG: n.sizeMS,
    paddingContentHorizontal: n.sizeMS,
    paddingContentVertical: n.sizeSM,
    paddingContentHorizontalSM: n.size,
    paddingContentVerticalSM: n.sizeXS,
    marginXXS: n.sizeXXS,
    marginXS: n.sizeXS,
    marginSM: n.sizeSM,
    margin: n.size,
    marginMD: n.sizeMD,
    marginLG: n.sizeLG,
    marginXL: n.sizeXL,
    marginXXL: n.sizeXXL,
    boxShadow: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowSecondary: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTertiary: `
      0 1px 2px 0 rgba(0, 0, 0, 0.03),
      0 1px 6px -1px rgba(0, 0, 0, 0.02),
      0 2px 4px 0 rgba(0, 0, 0, 0.02)
    `,
    screenXS: i,
    screenXSMin: i,
    screenXSMax: s - 1,
    screenSM: s,
    screenSMMin: s,
    screenSMMax: a - 1,
    screenMD: a,
    screenMDMin: a,
    screenMDMax: c - 1,
    screenLG: c,
    screenLGMin: c,
    screenLGMax: l - 1,
    screenXL: l,
    screenXLMin: l,
    screenXLMax: f - 1,
    screenXXL: f,
    screenXXLMin: f,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new Q("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new Q("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new Q("rgba(0, 0, 0, 0.09)").toRgbString()}
    `,
    boxShadowDrawerRight: `
      -6px 0 16px 0 rgba(0, 0, 0, 0.08),
      -3px 0 6px -4px rgba(0, 0, 0, 0.12),
      -9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerLeft: `
      6px 0 16px 0 rgba(0, 0, 0, 0.08),
      3px 0 6px -4px rgba(0, 0, 0, 0.12),
      9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerUp: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerDown: `
      0 -6px 16px 0 rgba(0, 0, 0, 0.08),
      0 -3px 6px -4px rgba(0, 0, 0, 0.12),
      0 -9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTabsOverflowLeft: "inset 10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowRight: "inset -10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowTop: "inset 0 10px 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowBottom: "inset 0 -10px 8px -8px rgba(0, 0, 0, 0.08)"
  }), o);
}
const oi = {
  lineHeight: !0,
  lineHeightSM: !0,
  lineHeightLG: !0,
  lineHeightHeading1: !0,
  lineHeightHeading2: !0,
  lineHeightHeading3: !0,
  lineHeightHeading4: !0,
  lineHeightHeading5: !0,
  opacityLoading: !0,
  fontWeightStrong: !0,
  zIndexPopupBase: !0,
  zIndexBase: !0,
  opacityImage: !0
}, ii = {
  size: !0,
  sizeSM: !0,
  sizeLG: !0,
  sizeMD: !0,
  sizeXS: !0,
  sizeXXS: !0,
  sizeMS: !0,
  sizeXL: !0,
  sizeXXL: !0,
  sizeUnit: !0,
  sizeStep: !0,
  motionBase: !0,
  motionUnit: !0
}, si = cr(pt.defaultAlgorithm), ai = {
  screenXS: !0,
  screenXSMin: !0,
  screenXSMax: !0,
  screenSM: !0,
  screenSMMin: !0,
  screenSMMax: !0,
  screenMD: !0,
  screenMDMin: !0,
  screenMDMax: !0,
  screenLG: !0,
  screenLGMin: !0,
  screenLGMax: !0,
  screenXL: !0,
  screenXLMin: !0,
  screenXLMax: !0,
  screenXXL: !0,
  screenXXLMin: !0
}, Bn = (e, t, r) => {
  const o = r.getDerivativeToken(e), {
    override: n,
    ...i
  } = t;
  let s = {
    ...o,
    override: n
  };
  return s = ri(s), i && Object.entries(i).forEach(([a, c]) => {
    const {
      theme: l,
      ...f
    } = c;
    let u = f;
    l && (u = Bn({
      ...s,
      ...f
    }, {
      override: f
    }, l)), s[a] = u;
  }), s;
};
function ci() {
  const {
    token: e,
    hashed: t,
    theme: r = si,
    override: o,
    cssVar: n
  } = C.useContext(pt._internalContext), [i, s, a] = lr(r, [pt.defaultSeed, e], {
    salt: `${Qr}-${t || ""}`,
    override: o,
    getComputedToken: Bn,
    cssVar: n && {
      prefix: n.prefix,
      key: n.key,
      unitless: oi,
      ignore: ii,
      preserve: ai
    }
  });
  return [r, a, t ? s : "", i, n];
}
const {
  genStyleHooks: li,
  genComponentStyleHook: Ai,
  genSubStyleComponent: $i
} = Zo({
  usePrefix: () => {
    const {
      getPrefixCls: e,
      iconPrefixCls: t
    } = vt();
    return {
      iconPrefixCls: t,
      rootPrefixCls: e()
    };
  },
  useToken: () => {
    const [e, t, r, o, n] = ci();
    return {
      theme: e,
      realToken: t,
      hashId: r,
      token: o,
      cssVar: n
    };
  },
  useCSP: () => {
    const {
      csp: e
    } = vt();
    return e ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
});
var ui = `accept acceptCharset accessKey action allowFullScreen allowTransparency
    alt async autoComplete autoFocus autoPlay capture cellPadding cellSpacing challenge
    charSet checked classID className colSpan cols content contentEditable contextMenu
    controls coords crossOrigin data dateTime default defer dir disabled download draggable
    encType form formAction formEncType formMethod formNoValidate formTarget frameBorder
    headers height hidden high href hrefLang htmlFor httpEquiv icon id inputMode integrity
    is keyParams keyType kind label lang list loop low manifest marginHeight marginWidth max maxLength media
    mediaGroup method min minLength multiple muted name noValidate nonce open
    optimum pattern placeholder poster preload radioGroup readOnly rel required
    reversed role rowSpan rows sandbox scope scoped scrolling seamless selected
    shape size sizes span spellCheck src srcDoc srcLang srcSet start step style
    summary tabIndex target title type useMap value width wmode wrap`, fi = `onCopy onCut onPaste onCompositionEnd onCompositionStart onCompositionUpdate onKeyDown
    onKeyPress onKeyUp onFocus onBlur onChange onInput onSubmit onClick onContextMenu onDoubleClick
    onDrag onDragEnd onDragEnter onDragExit onDragLeave onDragOver onDragStart onDrop onMouseDown
    onMouseEnter onMouseLeave onMouseMove onMouseOut onMouseOver onMouseUp onSelect onTouchCancel
    onTouchEnd onTouchMove onTouchStart onScroll onWheel onAbort onCanPlay onCanPlayThrough
    onDurationChange onEmptied onEncrypted onEnded onError onLoadedData onLoadedMetadata
    onLoadStart onPause onPlay onPlaying onProgress onRateChange onSeeked onSeeking onStalled onSuspend onTimeUpdate onVolumeChange onWaiting onLoad onError`, di = "".concat(ui, " ").concat(fi).split(/[\s\n]+/), mi = "aria-", hi = "data-";
function mn(e, t) {
  return e.indexOf(t) === 0;
}
function Gn(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : !1, r;
  t === !1 ? r = {
    aria: !0,
    data: !0,
    attr: !0
  } : t === !0 ? r = {
    aria: !0
  } : r = x({}, t);
  var o = {};
  return Object.keys(e).forEach(function(n) {
    // Aria
    (r.aria && (n === "role" || mn(n, mi)) || // Data
    r.data && mn(n, hi) || // Attr
    r.attr && di.includes(n)) && (o[n] = e[n]);
  }), o;
}
const lt = () => ({
  height: 0,
  opacity: 0
}), hn = (e) => {
  const {
    scrollHeight: t
  } = e;
  return {
    height: t,
    opacity: 1
  };
}, pi = (e) => ({
  height: e ? e.offsetHeight : 0
}), ut = (e, t) => (t == null ? void 0 : t.deadline) === !0 || t.propertyName === "height", gi = (e = eo) => ({
  motionName: `${e}-motion-collapse`,
  onAppearStart: lt,
  onEnterStart: lt,
  onAppearActive: hn,
  onEnterActive: hn,
  onLeaveStart: pi,
  onLeaveActive: lt,
  onAppearEnd: ut,
  onEnterEnd: ut,
  onLeaveEnd: ut,
  motionDeadline: 500
}), vi = (e, t, r) => {
  const [o, n, i] = C.useMemo(() => {
    let f = {
      expandedKeys: [],
      onExpand: () => {
      }
    };
    return e ? (typeof e == "object" && (f = {
      ...f,
      ...e
    }), [!0, f.expandedKeys, f.onExpand]) : [!1, f.expandedKeys, f.onExpand];
  }, [e]), [s, a] = so(n), c = (f) => {
    a((u) => {
      const d = u.includes(f) ? u.filter((h) => h !== f) : [...u, f];
      return i == null || i(d), d;
    });
  }, l = C.useMemo(() => o ? {
    ...gi(r),
    motionAppear: !1,
    leavedClassName: `${t}-content-hidden`
  } : {}, [r, t, o]);
  return [o, s, o ? c : void 0, l];
}, yi = (e) => ({
  [e.componentCls]: {
    // For common/openAnimation
    [`${e.antCls}-motion-collapse-legacy`]: {
      overflow: "hidden",
      "&-active": {
        transition: `height ${e.motionDurationMid} ${e.motionEaseInOut},
        opacity ${e.motionDurationMid} ${e.motionEaseInOut} !important`
      }
    },
    [`${e.antCls}-motion-collapse`]: {
      overflow: "hidden",
      transition: `height ${e.motionDurationMid} ${e.motionEaseInOut},
        opacity ${e.motionDurationMid} ${e.motionEaseInOut} !important`
    }
  }
});
let ft = /* @__PURE__ */ function(e) {
  return e.PENDING = "pending", e.SUCCESS = "success", e.ERROR = "error", e;
}({});
const Xn = /* @__PURE__ */ C.createContext(null), bi = (e) => {
  const {
    info: t = {},
    nextStatus: r,
    onClick: o,
    ...n
  } = e, i = Gn(n, {
    attr: !0,
    aria: !0,
    data: !0
  }), {
    prefixCls: s,
    collapseMotion: a,
    enableCollapse: c,
    expandedKeys: l,
    direction: f,
    classNames: u = {},
    styles: d = {}
  } = C.useContext(Xn), h = C.useId(), {
    key: v = h,
    icon: m,
    title: p,
    extra: b,
    content: S,
    footer: w,
    status: y,
    description: _
  } = t, g = `${s}-item`, M = () => o == null ? void 0 : o(v), T = l == null ? void 0 : l.includes(v);
  return /* @__PURE__ */ C.createElement("div", ue({}, i, {
    className: X(g, {
      [`${g}-${y}${r ? `-${r}` : ""}`]: y
    }, e.className),
    style: e.style
  }), /* @__PURE__ */ C.createElement("div", {
    className: X(`${g}-header`, u.itemHeader),
    style: d.itemHeader,
    onClick: M
  }, /* @__PURE__ */ C.createElement(sr, {
    icon: m,
    className: `${g}-icon`
  }), /* @__PURE__ */ C.createElement("div", {
    className: X(`${g}-header-box`, {
      [`${g}-collapsible`]: c && S
    })
  }, /* @__PURE__ */ C.createElement(jt.Text, {
    strong: !0,
    ellipsis: {
      tooltip: {
        placement: f === "rtl" ? "topRight" : "topLeft",
        title: p
      }
    },
    className: `${g}-title`
  }, c && S && (f === "rtl" ? /* @__PURE__ */ C.createElement(ur, {
    className: `${g}-collapse-icon`,
    rotate: T ? -90 : 0
  }) : /* @__PURE__ */ C.createElement(fr, {
    className: `${g}-collapse-icon`,
    rotate: T ? 90 : 0
  })), p), _ && /* @__PURE__ */ C.createElement(jt.Text, {
    className: `${g}-desc`,
    ellipsis: {
      tooltip: {
        placement: f === "rtl" ? "topRight" : "topLeft",
        title: _
      }
    },
    type: "secondary"
  }, _)), b && /* @__PURE__ */ C.createElement("div", {
    className: `${g}-extra`
  }, b)), S && /* @__PURE__ */ C.createElement(Fn, ue({}, a, {
    visible: c ? T : !0
  }), ({
    className: R,
    style: L
  }, I) => /* @__PURE__ */ C.createElement("div", {
    className: X(`${g}-content`, R),
    ref: I,
    style: L
  }, /* @__PURE__ */ C.createElement("div", {
    className: X(`${g}-content-box`, u.itemContent),
    style: d.itemContent
  }, S))), w && /* @__PURE__ */ C.createElement("div", {
    className: X(`${g}-footer`, u.itemFooter),
    style: d.itemFooter
  }, w));
}, Si = (e) => {
  const {
    componentCls: t
  } = e, r = `${t}-item`, o = {
    [ft.PENDING]: e.colorPrimaryText,
    [ft.SUCCESS]: e.colorSuccessText,
    [ft.ERROR]: e.colorErrorText
  }, n = Object.keys(o);
  return n.reduce((i, s) => {
    const a = o[s];
    return n.forEach((c) => {
      const l = `& ${r}-${s}-${c}`, f = s === c ? {} : {
        backgroundColor: "none !important",
        backgroundImage: `linear-gradient(${a}, ${o[c]})`
      };
      i[l] = {
        [`& ${r}-icon, & > *::before`]: {
          backgroundColor: `${a} !important`
        },
        "& > :last-child::before": f
      };
    }), i;
  }, {});
}, xi = (e) => {
  const {
    calc: t,
    componentCls: r
  } = e, o = `${r}-item`, n = {
    content: '""',
    width: t(e.lineWidth).mul(2).equal(),
    display: "block",
    position: "absolute",
    insetInlineEnd: "none",
    backgroundColor: e.colorTextPlaceholder
  };
  return {
    "& > :last-child > :last-child": {
      "&::before": {
        display: "none !important"
      },
      [`&${o}-footer`]: {
        "&::before": {
          display: "block !important",
          bottom: 0
        }
      }
    },
    [`& > ${o}`]: {
      [`& ${o}-header, & ${o}-content, & ${o}-footer`]: {
        position: "relative",
        "&::before": {
          bottom: t(e.itemGap).mul(-1).equal()
        }
      },
      [`& ${o}-header, & ${o}-content`]: {
        marginInlineStart: t(e.itemSize).mul(-1).equal(),
        "&::before": {
          ...n,
          insetInlineStart: t(e.itemSize).div(2).sub(e.lineWidth).equal()
        }
      },
      [`& ${o}-header::before`]: {
        top: e.itemSize,
        bottom: t(e.itemGap).mul(-2).equal()
      },
      [`& ${o}-content::before`]: {
        top: "100%"
      },
      [`& ${o}-footer::before`]: {
        ...n,
        top: 0,
        insetInlineStart: t(e.itemSize).div(-2).sub(e.lineWidth).equal()
      }
    }
  };
}, Ci = (e) => {
  const {
    componentCls: t
  } = e, r = `${t}-item`;
  return {
    [r]: {
      display: "flex",
      flexDirection: "column",
      [`& ${r}-collapsible`]: {
        cursor: "pointer"
      },
      [`& ${r}-header`]: {
        display: "flex",
        marginBottom: e.itemGap,
        gap: e.itemGap,
        alignItems: "flex-start",
        [`& ${r}-icon`]: {
          height: e.itemSize,
          width: e.itemSize,
          fontSize: e.itemFontSize
        },
        [`& ${r}-extra`]: {
          height: e.itemSize,
          maxHeight: e.itemSize
        },
        [`& ${r}-header-box`]: {
          flex: 1,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
          [`& ${r}-title`]: {
            height: e.itemSize,
            lineHeight: `${je(e.itemSize)}`,
            maxHeight: e.itemSize,
            fontSize: e.itemFontSize,
            [`& ${r}-collapse-icon`]: {
              marginInlineEnd: e.marginXS
            }
          },
          [`& ${r}-desc`]: {
            fontSize: e.itemFontSize
          }
        }
      },
      [`& ${r}-content`]: {
        [`& ${r}-content-hidden`]: {
          display: "none"
        },
        [`& ${r}-content-box`]: {
          padding: e.itemGap,
          display: "inline-block",
          maxWidth: `calc(100% - ${e.itemSize})`,
          borderRadius: e.borderRadiusLG,
          backgroundColor: e.colorBgContainer,
          border: `${je(e.lineWidth)} ${e.lineType} ${e.colorBorderSecondary}`
        }
      },
      [`& ${r}-footer`]: {
        marginTop: e.itemGap,
        display: "inline-flex"
      }
    }
  };
}, dt = (e, t = "middle") => {
  const {
    componentCls: r
  } = e, o = {
    large: {
      itemSize: e.itemSizeLG,
      itemGap: e.itemGapLG,
      itemFontSize: e.itemFontSizeLG
    },
    middle: {
      itemSize: e.itemSize,
      itemGap: e.itemGap,
      itemFontSize: e.itemFontSize
    },
    small: {
      itemSize: e.itemSizeSM,
      itemGap: e.itemGapSM,
      itemFontSize: e.itemFontSizeSM
    }
  }[t];
  return {
    [`&${r}-${t}`]: {
      paddingInlineStart: o.itemSize,
      gap: o.itemGap,
      ...Ci({
        ...e,
        ...o
      }),
      ...xi({
        ...e,
        ...o
      })
    }
  };
}, Ei = (e) => {
  const {
    componentCls: t
  } = e;
  return {
    [t]: {
      display: "flex",
      flexDirection: "column",
      ...Si(e),
      ...dt(e),
      ...dt(e, "large"),
      ...dt(e, "small"),
      [`&${t}-rtl`]: {
        direction: "rtl"
      }
    }
  };
}, _i = li("ThoughtChain", (e) => {
  const t = Rt(e, {
    // small size tokens
    itemFontSizeSM: e.fontSizeSM,
    itemSizeSM: e.calc(e.controlHeightXS).add(e.controlHeightSM).div(2).equal(),
    itemGapSM: e.marginSM,
    // default size tokens
    itemFontSize: e.fontSize,
    itemSize: e.calc(e.controlHeightSM).add(e.controlHeight).div(2).equal(),
    itemGap: e.margin,
    // large size tokens
    itemFontSizeLG: e.fontSizeLG,
    itemSizeLG: e.calc(e.controlHeight).add(e.controlHeightLG).div(2).equal(),
    itemGapLG: e.marginLG
  });
  return [Ei(t), yi(t)];
}), wi = (e) => {
  const {
    prefixCls: t,
    rootClassName: r,
    className: o,
    items: n,
    collapsible: i,
    styles: s = {},
    style: a,
    classNames: c = {},
    size: l = "middle",
    ...f
  } = e, u = Gn(f, {
    attr: !0,
    aria: !0,
    data: !0
  }), {
    getPrefixCls: d,
    direction: h
  } = vt(), v = d(), m = d("thought-chain", t), p = Zr("thoughtChain"), [b, S, w, y] = vi(i, m, v), [_, g, M] = _i(m), T = X(o, r, m, p.className, g, M, {
    [`${m}-rtl`]: h === "rtl"
  }, `${m}-${l}`);
  return _(/* @__PURE__ */ C.createElement("div", ue({}, u, {
    className: T,
    style: {
      ...p.style,
      ...a
    }
  }), /* @__PURE__ */ C.createElement(Xn.Provider, {
    value: {
      prefixCls: m,
      enableCollapse: b,
      collapseMotion: y,
      expandedKeys: S,
      direction: h,
      classNames: {
        itemHeader: X(p.classNames.itemHeader, c.itemHeader),
        itemContent: X(p.classNames.itemContent, c.itemContent),
        itemFooter: X(p.classNames.itemFooter, c.itemFooter)
      },
      styles: {
        itemHeader: {
          ...p.styles.itemHeader,
          ...s.itemHeader
        },
        itemContent: {
          ...p.styles.itemContent,
          ...s.itemContent
        },
        itemFooter: {
          ...p.styles.itemFooter,
          ...s.itemFooter
        }
      }
    }
  }, n == null ? void 0 : n.map((R, L) => {
    var I;
    return /* @__PURE__ */ C.createElement(bi, {
      key: R.key || `key_${L}`,
      className: X(p.classNames.item, c.item),
      style: {
        ...p.styles.item,
        ...s.item
      },
      info: {
        ...R,
        icon: R.icon || L + 1
      },
      onClick: w,
      nextStatus: ((I = n[L + 1]) == null ? void 0 : I.status) || R.status
    });
  }))));
}, Ti = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Mi(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const o = e[r];
    return t[r] = Pi(r, o), t;
  }, {}) : {};
}
function Pi(e, t) {
  return typeof t == "number" && !Ti.includes(e) ? t + "px" : t;
}
function wt(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const n = C.Children.toArray(e._reactElement.props.children).map((i) => {
      if (C.isValidElement(i) && i.props.__slot__) {
        const {
          portals: s,
          clonedElement: a
        } = wt(i.props.el);
        return C.cloneElement(i, {
          ...i.props,
          el: a,
          children: [...C.Children.toArray(i.props.children), ...s]
        });
      }
      return null;
    });
    return n.originalChildren = e._reactElement.props.children, t.push(mt(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: n
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((n) => {
    e.getEventListeners(n).forEach(({
      listener: s,
      type: a,
      useCapture: c
    }) => {
      r.addEventListener(a, s, c);
    });
  });
  const o = Array.from(e.childNodes);
  for (let n = 0; n < o.length; n++) {
    const i = o[n];
    if (i.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = wt(i);
      t.push(...a), r.appendChild(s);
    } else i.nodeType === 3 && r.appendChild(i.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function Oi(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const pn = Yn(({
  slot: e,
  clone: t,
  className: r,
  style: o,
  observeAttributes: n
}, i) => {
  const s = Z(), [a, c] = Jn([]), {
    forceClone: l
  } = rr(), f = l ? !0 : t;
  return pe(() => {
    var v;
    if (!s.current || !e)
      return;
    let u = e;
    function d() {
      let m = u;
      if (u.tagName.toLowerCase() === "svelte-slot" && u.children.length === 1 && u.children[0] && (m = u.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), Oi(i, m), r && m.classList.add(...r.split(" ")), o) {
        const p = Mi(o);
        Object.keys(p).forEach((b) => {
          m.style[b] = p[b];
        });
      }
    }
    let h = null;
    if (f && window.MutationObserver) {
      let m = function() {
        var w, y, _;
        (w = s.current) != null && w.contains(u) && ((y = s.current) == null || y.removeChild(u));
        const {
          portals: b,
          clonedElement: S
        } = wt(e);
        u = S, c(b), u.style.display = "contents", d(), (_ = s.current) == null || _.appendChild(u);
      };
      m();
      const p = Er(() => {
        m(), h == null || h.disconnect(), h == null || h.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: n
        });
      }, 50);
      h = new window.MutationObserver(p), h.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      u.style.display = "contents", d(), (v = s.current) == null || v.appendChild(u);
    return () => {
      var m, p;
      u.style.display = "", (m = s.current) != null && m.contains(u) && ((p = s.current) == null || p.removeChild(u)), h == null || h.disconnect();
    };
  }, [e, f, r, o, i, n]), C.createElement("react-child", {
    ref: s,
    style: {
      display: "contents"
    }
  }, ...a);
});
function Un(e, t, r) {
  const o = e.filter(Boolean);
  if (o.length !== 0)
    return o.map((n, i) => {
      var l;
      if (typeof n != "object")
        return t != null && t.fallback ? t.fallback(n) : n;
      const s = {
        ...n.props,
        key: ((l = n.props) == null ? void 0 : l.key) ?? (r ? `${r}-${i}` : `${i}`)
      };
      let a = s;
      Object.keys(n.slots).forEach((f) => {
        if (!n.slots[f] || !(n.slots[f] instanceof Element) && !n.slots[f].el)
          return;
        const u = f.split(".");
        u.forEach((b, S) => {
          a[b] || (a[b] = {}), S !== u.length - 1 && (a = s[b]);
        });
        const d = n.slots[f];
        let h, v, m = (t == null ? void 0 : t.clone) ?? !1, p = t == null ? void 0 : t.forceClone;
        d instanceof Element ? h = d : (h = d.el, v = d.callback, m = d.clone ?? m, p = d.forceClone ?? p), p = p ?? !!v, a[u[u.length - 1]] = h ? v ? (...b) => (v(u[u.length - 1], b), /* @__PURE__ */ ee.jsx($t, {
          params: b,
          forceClone: p,
          children: /* @__PURE__ */ ee.jsx(pn, {
            slot: h,
            clone: m
          })
        })) : /* @__PURE__ */ ee.jsx($t, {
          forceClone: p,
          children: /* @__PURE__ */ ee.jsx(pn, {
            slot: h,
            clone: m
          })
        }) : a[u[u.length - 1]], a = s;
      });
      const c = (t == null ? void 0 : t.children) || "children";
      return n[c] ? s[c] = Un(n[c], t, `${i}`) : t != null && t.children && (s[c] = void 0, Reflect.deleteProperty(s, c)), s;
    });
}
const {
  useItems: Ri,
  withItemsContextProvider: Li,
  ItemHandler: ji
} = or("antdx-thought-chain-items"), zi = qr(Li(["default", "items"], ({
  children: e,
  items: t,
  ...r
}) => {
  const {
    items: o
  } = Ri(), n = o.items.length > 0 ? o.items : o.default;
  return /* @__PURE__ */ ee.jsxs(ee.Fragment, {
    children: [/* @__PURE__ */ ee.jsx("div", {
      style: {
        display: "none"
      },
      children: e
    }), /* @__PURE__ */ ee.jsx(wi, {
      ...r,
      items: Zn(() => t || Un(n, {
        clone: !0
      }), [t, n])
    })]
  });
}));
export {
  zi as ThoughtChain,
  zi as default
};
