import { i as ue, a as W, r as de, g as fe, w as R, b as me } from "./Index-c-voGoVV.js";
const y = window.ms_globals.React, ie = window.ms_globals.React.useMemo, le = window.ms_globals.React.forwardRef, ce = window.ms_globals.React.useRef, ae = window.ms_globals.React.useState, $ = window.ms_globals.React.useEffect, N = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, D = window.ms_globals.internalContext.ContextPropsProvider, U = window.ms_globals.antd.Form;
var _e = /\s/;
function he(e) {
  for (var t = e.length; t-- && _e.test(e.charAt(t)); )
    ;
  return t;
}
var ge = /^\s+/;
function we(e) {
  return e && e.slice(0, he(e) + 1).replace(ge, "");
}
var z = NaN, be = /^[-+]0x[0-9a-f]+$/i, ye = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, xe = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return z;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var o = ye.test(e);
  return o || Ee.test(e) ? xe(e.slice(2), o ? 2 : 8) : be.test(e) ? z : +e;
}
var F = function() {
  return de.Date.now();
}, ve = "Expected a function", Ce = Math.max, Ie = Math.min;
function Se(e, t, o) {
  var i, s, n, r, l, a, p = 0, _ = !1, c = !1, h = !0;
  if (typeof e != "function")
    throw new TypeError(ve);
  t = B(t) || 0, W(o) && (_ = !!o.leading, c = "maxWait" in o, n = c ? Ce(B(o.maxWait) || 0, t) : n, h = "trailing" in o ? !!o.trailing : h);
  function m(d) {
    var b = i, S = s;
    return i = s = void 0, p = d, r = e.apply(S, b), r;
  }
  function E(d) {
    return p = d, l = setTimeout(w, t), _ ? m(d) : r;
  }
  function f(d) {
    var b = d - a, S = d - p, M = t - b;
    return c ? Ie(M, n - S) : M;
  }
  function g(d) {
    var b = d - a, S = d - p;
    return a === void 0 || b >= t || b < 0 || c && S >= n;
  }
  function w() {
    var d = F();
    if (g(d))
      return x(d);
    l = setTimeout(w, f(d));
  }
  function x(d) {
    return l = void 0, h && i ? m(d) : (i = s = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), p = 0, i = a = s = l = void 0;
  }
  function u() {
    return l === void 0 ? r : x(F());
  }
  function C() {
    var d = F(), b = g(d);
    if (i = arguments, s = this, a = d, b) {
      if (l === void 0)
        return E(a);
      if (c)
        return clearTimeout(l), l = setTimeout(w, t), m(a);
    }
    return l === void 0 && (l = setTimeout(w, t)), r;
  }
  return C.cancel = v, C.flush = u, C;
}
var ee = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Re = y, ke = Symbol.for("react.element"), Oe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, Pe = Re.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Te.call(t, i) && !Fe.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: ke,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Pe.current
  };
}
P.Fragment = Oe;
P.jsx = te;
P.jsxs = te;
ee.exports = P;
var T = ee.exports;
const {
  SvelteComponent: Le,
  assign: G,
  binding_callbacks: H,
  check_outros: Ne,
  children: ne,
  claim_element: re,
  claim_space: We,
  component_subscribe: q,
  compute_slots: je,
  create_slot: Ae,
  detach: I,
  element: oe,
  empty: K,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Me,
  get_slot_changes: De,
  group_outros: Ue,
  init: ze,
  insert_hydration: k,
  safe_not_equal: Be,
  set_custom_element_data: se,
  space: Ge,
  transition_in: O,
  transition_out: j,
  update_slot_base: He
} = window.__gradio__svelte__internal, {
  beforeUpdate: qe,
  getContext: Ke,
  onDestroy: Je,
  setContext: Ve
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Ae(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && He(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Me(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (O(s, n), o = !0);
    },
    o(n) {
      j(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function Xe(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), o = Ge(), n && n.c(), i = K(), this.h();
    },
    l(r) {
      t = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(I), o = We(r), n && n.l(r), i = K(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && O(n, 1)) : (n = V(r), n.c(), O(n, 1), n.m(i.parentNode, i)) : n && (Ue(), j(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      s || (O(n), s = !0);
    },
    o(r) {
      j(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function X(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ye(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = je(n);
  let {
    svelteInit: a
  } = t;
  const p = R(X(t)), _ = R();
  q(e, _, (u) => o(0, i = u));
  const c = R();
  q(e, c, (u) => o(1, s = u));
  const h = [], m = Ke("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: g
  } = fe() || {}, w = a({
    parent: m,
    props: p,
    target: _,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: g,
    onDestroy(u) {
      h.push(u);
    }
  });
  Ve("$$ms-gr-react-wrapper", w), qe(() => {
    p.set(X(t));
  }), Je(() => {
    h.forEach((u) => u());
  });
  function x(u) {
    H[u ? "unshift" : "push"](() => {
      i = u, _.set(i);
    });
  }
  function v(u) {
    H[u ? "unshift" : "push"](() => {
      s = u, c.set(s);
    });
  }
  return e.$$set = (u) => {
    o(17, t = G(G({}, t), J(u))), "svelteInit" in u && o(5, a = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, t = J(t), [i, s, _, c, l, a, r, n, x, v];
}
class Qe extends Le {
  constructor(t) {
    super(), ze(this, t, Ye, Xe, Be, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, L = window.ms_globals.tree;
function Ze(e, t = {}) {
  function o(i) {
    const s = R(), n = new Qe({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? L;
          return a.nodes = [...a.nodes, l], Y({
            createPortal: N,
            node: L
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((p) => p.svelteInstance !== s), Y({
              createPortal: N,
              node: L
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function $e(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function et(e, t = !1) {
  try {
    if (me(e))
      return e;
    if (t && !$e(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Q(e, t) {
  return ie(() => et(e, t), [e, t]);
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = rt(o, i), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function A(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = A(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(N(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: a
    }) => {
      o.addEventListener(l, r, a);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = A(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function ot(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const st = le(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ce(), [l, a] = ae([]), {
    forceClone: p
  } = pe(), _ = p ? !0 : t;
  return $(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function h() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), ot(n, f), o && f.classList.add(...o.split(" ")), i) {
        const g = nt(i);
        Object.keys(g).forEach((w) => {
          f.style[w] = g[w];
        });
      }
    }
    let m = null;
    if (_ && window.MutationObserver) {
      let f = function() {
        var v, u, C;
        (v = r.current) != null && v.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: w,
          clonedElement: x
        } = A(e);
        c = x, a(w), c.style.display = "contents", h(), (C = r.current) == null || C.appendChild(c);
      };
      f();
      const g = Se(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(g), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", h(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var f, g;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((g = r.current) == null || g.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, _, o, i, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function Z(e, t) {
  return e ? /* @__PURE__ */ T.jsx(st, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function it({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ T.jsx(D, {
    params: s,
    forceClone: !0,
    children: Z(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ T.jsx(D, {
    params: s,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const ct = Ze(({
  value: e,
  onValueChange: t,
  requiredMark: o,
  onValuesChange: i,
  feedbackIcons: s,
  setSlotParams: n,
  slots: r,
  ...l
}) => {
  const [a] = U.useForm(), p = Q(s), _ = Q(o);
  return $(() => {
    a.setFieldsValue(e);
  }, [a, e]), /* @__PURE__ */ T.jsx(U, {
    ...l,
    initialValues: e,
    form: a,
    requiredMark: r.requiredMark ? it({
      key: "requiredMark",
      setSlotParams: n,
      slots: r
    }) : o === "optional" ? o : _ || o,
    feedbackIcons: p,
    onValuesChange: (c, h) => {
      t(h), i == null || i(c, h);
    }
  });
});
export {
  ct as Form,
  ct as default
};
